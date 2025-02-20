PLACEHOLDER="[name]";

with open("invited_name.txt",'r') as names_list:
    names= names_list.readlines()
with open("starting_letter.docx") as letter_file:
    letter_contetnts=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contetnts.replace(PLACEHOLDER,stripped_name)
        
        with open(f"letter_for_{stripped_name}.docx",'w+') as completed_letter:
            completed_letter.write(new_letter) # type: ignore