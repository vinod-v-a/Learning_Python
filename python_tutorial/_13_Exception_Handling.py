"""
try:
    # Code that might cause an exception
except ExceptionType as e:
    # Code to handle the exception
else:
    # Executes if try block does NOT raise any exception
finally:
    # Always executes (whether exception occurred or not)
"""

# try:
# file2 = open("demo.txt", "x")
# data2 = file2.write("hello")
# file = open("new.txt", "r")
# data = file.read()
#     x = 10 / 0
#     print(x)
#     dc = {"a": 10}
#     print(dc["b"])
#     ls = [10, 20]
#     print(ls[3] * 5)
# except Exception as e:
#     print("Exception: ", e)
# except (IndexError, KeyError, ZeroDivisionError, FileNotFoundError, FileExistsError) as ue:  # multiple exception in tuple
#     print("unknown error", ue)
# except IndexError as ie:
#     print("IndexError: ", ie)
# except KeyError as ke:
#     print("KeyError: ", ke)
# except ZeroDivisionError as ze:
#     print("ZeroDivisionError: ", ze)
# except FileNotFoundError as fe:
#     print("FileNotFoundError: ", fe)
# except FileExistsError as fee:
#     print("FileExistsError: ", fee)


"============================== raise ==================================="

# def check_age(age):
#     if not isinstance(age, int):
#         raise TypeError("age must be in int")
#     return age
#
#
# # check_age("25")
# try:
#     print(check_age("25"))
#     # print(check_age(25))
# except TypeError as te:
#     print(te)

"========================= CustomError ======================="


# class CustomError(Exception):
#     pass
#
#
# def age_check(age):
#     if not isinstance(age, int):
#         raise CustomError("Age must  be int")
#     return age
#
#
# try:
#     print(age_check("25"))
# except CustomError as ce:
#     print(ce)

# Custom error with attribute

# class CustomError(Exception):
#     def __init__(self,message, age):
#         self.age = age
#         self.message = message
#
# def age_check(age):
#     if not isinstance(age, int):
#         raise CustomError("Age must  be int", type(age))
#     return age
#
# try:
#     print(age_check("25"))
# except CustomError as ce:
#     print(ce)

"=============================================================="
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                try:
                    number = int(line)
                    result = 100 / number
                    print(f"Line {line_number}: 100 / {number} = {result}")
                except ZeroDivisionError:
                    print(f"Line {line_number}: Error - Division by zero.")
                except ValueError:
                    print(f"Line {line_number}: Error - Invalid integer value.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Run the function
process_file('exception_example.txt')