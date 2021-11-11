import sys, os
import auth
import user_view, admin_view
import models
import database

USER_VIEW = user_view.User_view()
ADMIN_VIEW = admin_view.Admin_view()


print(" Enter '1' to Login as User or '2' to Login as Admin or 'Q' to Quit.... ")
action = input(" ==> ")

while action not in ['1','2','Q']:
    print(" Enter '1' to Login as User or '2' to Login as Admin or 'Q' to Quit.... ")
    action = input(" ==> ")
else:
    pass

if action == '1':
    USER_VIEW.home_page()

else:
    ADMIN_VIEW.login_page()
