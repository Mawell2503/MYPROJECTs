# Creating package diagram for HBnB application
    ~layers
        !1.Presentation Layer - the waiter
            handles user requests

            ~services
                ## A service is where the system does real work and makes decisions
                ## Services executes features (features = what the app offers)

            ~API endpoints
                ## A URL + HTTP method that accpets request and returns responses

        !2.Business Logic Layer - the kitchen
            does the actual work

            ~user
            ~place
            ~review
            ~amenity

        !3.Persistence Layer - the pantry/storage
            saves and retrieves data
            
            ~DAO(Database Access Objects)/ Repositories
                ## Classes and modules who talks to the database
                ## The part of the appp that fetches, save, updates, or deletes data
                
        ## These layers dont talk to eachother in a messy way. They use facade patterns

        ~facade patterns
            ## The facade pattern provides a unified,simple interface to a complex subsystem
            its like calling a receptionist at a hotel for housekeeping, security, etc.


      