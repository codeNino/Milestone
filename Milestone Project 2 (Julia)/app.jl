include("./views.jl")
include("./Auth.jl")

using .views
using .Auth

printstyled(" Serving Nigeria, One Transaction at a time.\n Press any key to continue....... \n ==> "; color = :green)
readline()
println(" Welcome to Charis Bank..\n Please Enter your UserName to proceed ")

name = readline()

user_exists = verify_userID(name)

while !user_exists
    println("UserName does not exist......\n")
    println("\n Please Enter  '1'  to Try again with a valid UserName or Enter '2' to Register as a new user \n ==>  ")
    action = readline()
    if action !== "2"
        println(" Please Enter your Username to continue \n  ")
        global name = readline()
        if verify_userID(name)
            break
        end
    else
        name = register_user()
        global user_exists = verify_userID(name)
        if user_exists
            break
        end
    end
end

println(" Please enter your secret password \n  ==> ")

pwd = readline()

authenticated = verify_userPWD(pwd)

while !authenticated
    println(" INVALID PASSWORD....Please Try Again with correct Password or Enter 'Q' TO Quit")
    println(" ==>  ")
    action = readline()
    if action === "Q"
        clear()
        exit()
    else
        println(" Please Enter your secret Password:  \n ==>  ")
        pwd = readline()
        global authenticated = verify_userPWD(pwd)
        if authenticated
            break
        end
    end
end


first_name = split(usersDB[name]["name"])[1]

printstyled(" Welcome $first_name to Charis Bank \n"; color = :green)

choice = transactions_view()

while choice === "A" || choice === "B" || choice === "C" || choice === "D"
    if choice === "A"
        global choice = instant_tranfer_view(name)

    elseif choice === "B"
        global choice = Airtime_Recharge(name)

    elseif choice === "C"
        global choice = make_withdrawal(name)

    elseif choice === "D"
        global choice = check_balance(name)
    end
end

