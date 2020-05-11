
import FBvalid
import FBinvalidUSER
import FBinvalidPASSWORD

first = FBvalid.FBvalid()
first.FB_log_in_valid_details_test()

second = FBinvalidUSER.FBinvalidUSER()
second.FB_log_in_invalid_username_test()

third = FBinvalidPASSWORD.FBinvalidPASSWORD()
third.FB_log_in_invalid_password_test()



