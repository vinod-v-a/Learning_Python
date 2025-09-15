"======================== Debugging ===================================="
# 1. Print()
# 2. pdb
# 3.breakpoint()
# 4.IDE - UI


"===================== Print() =============================="


# class CountStep:
#     cls_step = ""
#     print(f"Debugging line 13 : {cls_step}")
#
#     def count_step_meth(self, step):
#         print(f"Debuggingline 15 : {CountStep.cls_step}")
#         for each in range(step):
#             CountStep.cls_step += str(each)
#             print(f"Debugging line 18 : {CountStep.cls_step}")
#         return CountStep.cls_step
#
#
# cs_obj = CountStep()
# print(cs_obj.count_step_meth(10))

"==================== pdb =========================="


# from _12_01_Debugging import sum
#
# def reverse_string(input_str):
#     res = ""
#     import pdb; pdb.set_trace()
#     # breakpoint()
#     for each in input_str:
#
#         res += each
#     val = sum(5)
#     import pdb;pdb.set_trace()
#     # breakpoint()
#     x = {
#     "merchantOrderId": "TX123456",
#     "amount": 1000,
#     "expireAfter": 1200,
#     "metaInfo": {
#         "udf1": "additional-information-1",
#         "udf2": "additional-information-2",
#         "udf3": "additional-information-3",
#         "udf4": "additional-information-4",
#         "udf5": "additional-information-5"
#     },
#     "paymentFlow": {
#         "type": "PG_CHECKOUT",
#         "message": "Payment message used for collect requests",
#         "merchantUrls": {
#             "redirectUrl": ""
#         }
#     }
# }
#     import pdb;pdb.set_trace()
#     return res
#
# print(reverse_string("python"))


"========================== logging  ======================================"
# import logging
#
# logging.basicConfig(format="%(levelname)s :: %(asctime)s :: %(lineno)s :: %(message)s :: %(filename)s",
#                     handlers=[logging.StreamHandler(), logging.FileHandler("test.log")], level=logging.DEBUG)
#
#
# # logger = logging.getLogger("mylogger")
# logger = logging.getLogger("transactions")
#
# logger.debug("from DEBUG")
# logger.info("from INFO")
# logger.warning("from WARNING")
# logger.error("from ERROR")
# logger.critical("from CRITICAL")
"========================================================================================="


# import logging
#
# # Set up logging configuration
# logging.basicConfig(
#     level=logging.DEBUG,  # Minimum level to capture
#     format="%(levelname)s :: %(asctime)s :: %(message)s"
# )
#
# def process_payment(user, amount, balance):
#     logging.debug(f"process_payment() called with user={user}, amount={amount}, balance={balance}")
#
#     if not user:
#         logging.critical("No user provided! Cannot proceed with transaction.")
#         return
#
#     logging.info(f"User '{user}' initiated a transaction of ₹{amount}")
#
#     if amount <= 0:
#         logging.warning("Attempted transaction with non-positive amount.")
#         return
#
#     if amount > balance:
#         logging.error("Insufficient balance for the transaction.")
#         return
#
#     # Simulate success
#     balance -= amount
#     logging.info(f"Transaction successful! New balance: ₹{balance}")
#     return balance
#
# # Run test cases
# process_payment("alice", 0, 5000)         # WARNING: invalid amount
# process_payment("bob", 6000, 5000)        # ERROR: insufficient balance
# process_payment("charlie", 3000, 5000)    # INFO: success
# process_payment("", 1000, 5000)           # CRITICAL: no user


"============================================================================================"
import logging

logging.basicConfig(level=logging.DEBUG)

def divide(a, b):
    logging.debug(f"Inputs - a {a}, b {b}")
    if b == 0:
        logging.error("Attempted division by zero")
        return None
    result = a/b
    logging.info(f"Division result {result}")
    return result

divide(10, 2)
divide(10, 0)