module models

    

    mutable struct User
        name::String
        email::String
        username::String
        contact::String
        password::String
    end
    
    
    export User

end