Stage_Method_Template = (
    "\r{stage_method_definition}"
    "\n\t\"\"\""
    "\n\t{stage_method_docstring}"
    "\n\t\"\"\""
    "\n\n\t"
    "{code_before_inherited_code}"
    "\n\t{inherited_code_start}"
    "{code_after_inherited_code}"
    )
Stages_Definition = {
    "Stage1": {
        "stage_method_definition": "def stage1_method_definition",
        "stage_method_docstring":  "Paste documentatio here",
        "code_before_inherited_code": "{stage_methods}",
        "inherited_code_start": "",
        "code_after_inherited_code": "",
    },
    "Stage2": {
        "stage_method_definition": "def stage2_method_definition",
        "stage_method_docstring":  "Paste documentatio here",
        "code_before_inherited_code": "{stage_methods}",
        "inherited_code_start": "",
        "code_after_inherited_code": "",
    },
    "Stage3": {
        "stage_method_definition": "def stage3_method_definition",
        "stage_method_docstring":  "Paste documentation here",
        "code_before_inherited_code": "{stage_methods}",
        "inherited_code_start": "",
        "code_after_inherited_code": "",
    },
}