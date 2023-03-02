class Student:
    """
    Declare employee class to read and print data from a file
    """
    def __init__(self, name, email, post):
      self.name = name
      self.email = email
      self.post = post

    def __str__(self):
        return f'{self.name})'
        # return f'Person({self.first_name},{self.last_name},{self.age})'

    # def __str__(self):
    #   print('Student Information:')
    #   print('Name  :', self.name)
    #   print('Email  :', self.email)
    #   print('Post :', self.post)

# Defining main function
def main():
  hans = Student('Hans', '@', 'Cohort2')
  print(hans)     
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()     