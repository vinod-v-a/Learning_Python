import re
"============================ Phone Number ====================="
# design = r'\+91-[6-9]\d{9}'
# phone_pattern = re.compile(design)
#
# phone_number = "+91-6876543210asdfgh"
#
# print(phone_pattern.search(phone_number))

# if phone_pattern.fullmatch(phone_number):
#     print("Valid phone number")
# else:
#     print("Invalid phone number")


"============ Pan Card =============="

# design =r'^[A-Z]{5}[0-9]{4}[A-Z]$'
#
# pan_pattern = re.compile(design)
#
# pan_num = "AAAAA9999A"
#
# print(pan_pattern.fullmatch(pan_num))


"====================== Aadhaar Card ==================="
# design = r'^[2-9][0-9]{11}$'
#
# ac_pattern = re.compile(design)
#
# ac_num = "234567890123"
#
# print(ac_pattern.search(ac_num))


"========================= KA number plate ==================="

# design = r'^KA[0-9]{2}[A-Z]{2}[0-9]{4}$'
#
#
# ka_num_pattern = re.compile(design)
# sample_num = "KA01AB1234"
#
# print(ka_num_pattern.search(sample_num))



"====================   IFSC Code (Indian Bank Code) ============="

# design = r'^[A-Z]{4}0[0-9]{6}$'
#
# ifsc_pattern = re.compile(design)
#
# ifsc_code = "SBIN0005900"
#
# res = ifsc_pattern.match(ifsc_code)
# print(res)

"=================  Strong Password ======================"

# design = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[a-zA-Z\d@$!%*?&]{8,}$'
#
#
# password_pattern = re.compile(design)
# sample_password = "Pass@1234"
#
# print(password_pattern.fullmatch(sample_password))

print(2%5)



