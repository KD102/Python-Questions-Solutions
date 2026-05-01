"""

 Qutions : Write a program to fill in a letter template given below with name and date.
               letter
                 Dear <|Name | >,
                  You are selected!
                   <| Date |>

"""

latter = """
        Dear <|Name|>,
            You are selected!
            <|Date|>
        """
print(latter.replace("<|Name|>","Kenil Dhanani").replace("<|Date|>","06/07/2025"))