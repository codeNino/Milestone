module models    

    mutable struct User
        name::String
        email::String
        username::String
        contact::String
        password::String
    end

    mutable struct Admin
        name::String
        email::String
        password::String
    end

    
    export User

end