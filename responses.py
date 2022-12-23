import string


def handle_response(message) -> str:
    p_message = message.lower()
    
    if "max" in p_message:
        f = open("yarrak.txt",'r') 
        data = f.read() 
        counter = int(data)   
        
        datatowrite =str(counter + 1) 
        a = open("yarrak.txt",'w')
        a.write(datatowrite) 
        a.close()
        return message
    
    if p_message == "counter":
        f = open("yarrak.txt",'r') 
        data = f.read() 
        if not len(data) > 0: 

          counter = 0
        else:
          counter = int(data)
        return str(counter) + " kere max."
    
    if p_message == "borağ":
      
      return "efe(zoomeg) ve aral borayı sikeyim."
    
    if p_message == "niggers":
      return "I hate niggers"
    
    if p_message == "zzzzz":
      return "documentation yok ozan sorma"
    
    if p_message == "mahmut, ozan hakkında ne düşünüyorsun?":
      return "OZAN MI????? O acayip cringe birisi ve 1984 gibi benim ne yaptığımı bilmek istiyor hayır okumadım kitabı ama..."
    
    if p_message == "mahmut, tuğrul hakkında ne düşünüyorsun?":
      return "direkt allahım"
    
    if p_message == "mahmut, bora hakkında ne düşünüyorsun?":
      return "based birisi ama underage arkadaşları o kadar based değil"