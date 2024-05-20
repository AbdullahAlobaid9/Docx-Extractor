import re 

# targeted sybmols: (), {}, [], !@#$%^&*
# remove new_lines to make the texts organized remove(\n)

def clean_text(txt:str) -> str:
    return re.sub(r"[()\[\]{}!@#$%^&*]", "", txt).replace("\n", " ")


def main():
    sample_text = "hello (this) is a {text} from [hell] @!#$%^&* don't !@# be scared %$^&*"
    print(clean_text(sample_text))


if __name__ == "__main__":
    main()