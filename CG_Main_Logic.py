from CG_Methods_Set import Methods_Set_Dictionary
from CG_Methods_Parameters import Methods_Parameters
from CG_Stages_Set import Stage_Method_Template, Stages_Definition
"""
Nos referiremos al nombre de la etapa (stage_name) y a las instrucciones 
de etapa (stage_instructions) como etapa (stage).
Nos referiremos como conjunto de etapas como instrucciones "instructions".

stage: {stage_name, stage_instructions}
instructions: {stage1, stage2, stage3,...,stageN}
"""

class CodeGenerator:

    def __init__(self, instructions_set):
        self.instructions_set = instructions_set
        # Parsear las instrucciones. 
        self._current_stage_name = ""
        self._current_gv1 = ""
        self._current_gv2 = ""
        self._current_gv3 = ""

    @property
    def current_stage_name(self):
        return self._current_stage_name

    @current_stage_name.setter
    def current_stage_name(self, stage_name):
        self._current_stage_name = stage_name
    
    @property
    def current_gv1(self):
        return self._current_gv1
    
    @current_gv1.setter
    def current_gv1(self, current_gv1):
        self._current_gv1 = current_gv1

    @property
    def current_gv2(self):
        return self._current_gv2
    
    @current_gv2.setter
    def current_gv2(self, current_gv2):
        self._current_gv2 = current_gv2

    @property
    def current_gv3(self):
        return self._current_gv3
    
    @current_gv3.setter
    def current_gv3(self, current_gv3):
        self._current_gv3 = current_gv3

    def divide_instructions_into_stages(self):
        stage_name_list = []
        stage_instructions_list = []
        for stage in self.instructions_set.split("|"):
            splited_stage = stage.split(":")
            stage_name_list.append(splited_stage[0])
            stage_instructions_list.append(splited_stage[1]) 
        return stage_name_list, stage_instructions_list
    
    def build_stage_code(self):
        stages_implementation = ""
        stage_name_list, stage_instructions = self.divide_instructions_into_stages()
        for index in range(0, len(stage_name_list)):

            # Obtener la definicion del método (etapa)
            self.current_stage_name = stage_name_list[index]

            # Mapeo entre las instrucciones y los metodos. 
            stage_methods = self.map_methods_code(stage_instructions[index])
            
            # Embeber la definición de la etapa y sus metodos en el template. 
            stage_implementation = self.embed_methods_into_stage(self.current_stage_name, stage_methods)
            #print(stage_implementation)

            # Concatenar las etapas en una unica variable.
            stages_implementation = stages_implementation + stage_implementation
        
        return stages_implementation

    def map_methods_code(self, stage_instructions):
        lower_index = 0
        stage_instruction_method = ""
        stage_instructions_list = stage_instructions.split(',')
        number_of_stage_instructions = len(stage_instructions_list)
        #print(stage_instructions_list)

        while lower_index < number_of_stage_instructions:
            is_method = False
            for upper_index in range(number_of_stage_instructions, lower_index, -1):
                stage_instructions_subset = ",".join(stage_instructions_list[lower_index:upper_index])
                is_method = Methods_Set_Dictionary.get(stage_instructions_subset)
                #print(stage_instructions_subset)
                
                if is_method:
                    # TODO: Set method parameters based on global variables.
                    #update_global_parameters(verification)
                    parameters = Methods_Parameters.get(stage_instructions_subset)
                    #print(parameters)
                    stage_instruction_method += is_method["method"].format(**parameters)
                    #print(stage_instruction_method)
                    # update global variables
                    self.update_gloval_variables(
                        is_method.get("gv3"), 
                        is_method.get("gv2"), 
                        is_method.get("gv1"),
                        )
                    lower_index = upper_index
                    is_method = True
                    break

            if not is_method:
                lower_index += 1
        #print(stage_instruction_method)
        return stage_instruction_method
    

    def update_gloval_variables(self, gv3, gv2, gv1):
        if gv3 is not None:
            self._current_gv3 = gv3
            #print(f"Current gv3 is {self._current_gv3}")
        if gv2 is not None:
            self._current_gv2 = gv2
            #print(f"Current gv2 is {self._current_gv2}")
        if gv1 is not None:
            self._current_gv1 = gv1
            #print(f"Current gv1 is {self._current_gv1}")

    def embed_methods_into_stage(self, current_stage_name, stage_methods):

        stage_implementation = ""
        print(stage_methods)
        # TODO: Setear los diccionarios Stage_Definition.
        Stage = Stages_Definition.get(current_stage_name)
        Stage["code_before_inherited_code"] = Stage["code_before_inherited_code"].format(stage_methods=stage_methods)
        stage_implementation = Stage_Method_Template.format(**Stage)
        return stage_implementation



if __name__ == '__main__':
    instructions = (
#    "Base: Upgrade|"
    "Stage1:Instruction1,Instruction2,Instruction3|"
    "Stage2:Instruction4|"
    "Stage3:Instruction5,Instruction6,Instruction4,Instruction7"
    )
    test = CodeGenerator(instructions)
    stages_implementation = test.build_stage_code()
    print(stages_implementation)




