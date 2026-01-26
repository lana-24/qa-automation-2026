from tests import authentication_user ,users ,repos , issues ,searchh,rate_limit

def run():
    
    #print("\n","="*20,'auth','='*20)
    #authentication_user.run_all()
    
    #print("\n","="*20,'users','='*20)
    #users.run_all()
    
    #print("\n","="*20,'repos','='*20)
    #repos.run_all()

    print("\n","="*20,'issues','='*20)
    issues.run_all()
    
    #print("\n","="*20,'search','='*20)
    #searchh.run_all()
    
    print("\n","="*20,'search','='*20)
    rate_limit.run_all()
    
    
if __name__ == "__main__":
    run()
