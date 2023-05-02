# letter madha***
letter='''Dear <|bsdk|>,
          you are invited to oyo
          on ocassion of ladchatyi week
          so,came with <|madha**yaar's|>
          hope you will come
          you are chutiya oyo manager
          <|ladchat|>
          date: <|date|>
          sathan: <|field of sugarcane|>
          thanks'''
name=input('enter enter of mitra')
yaars=input('type of week')
manager=input('manager name')
date=input('date')
sathan=input('place name')
letter=letter.replace("<|bsdk|>",name)
letter=letter.replace("<|madha**yaar's|>",yaars)
letter=letter.replace("<|ladchat|>",manager)
letter=letter.replace("<|date|>",date)
letter=letter.replace("<|field of sugarcane|>",sathan)

print(letter)
