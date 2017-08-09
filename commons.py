# _    ___    __   _  _  ____  ____  _____  __  __  ____  __   
#( \  / __)  /__\ ( \/ )(  _ \( ___)(  _  )(  )(  )(_  _)(  )  
# \ \ \__ \ /(__)\ \  /  )   / )__)  )(_)(  )(__)(  _)(_  )(__ 
#  \_)(___/(__)(__)(__) (_)\_)(____)(___/\\(______)(____)(____)
#
#
#                        SAYREQUIL

namei=""
descriptioni=""
versioni=0

def printc(msg)
  txt="".join(["Commons Output:",msg])
  print(txt)

class cmd:
  def setup(name="My Game",desc="The best game.",version=1.00):
    namei=name
    descriptioni=desc
    versioni=version
    
  def define(content,name,args)
    if name is None:
      printc("No command name found")
      return 400
      exit()
    else:
      printc("Command name is ok")
    
    if content is None:
      printc("No content found.")
      return 402
      exit()
    else:
      printc("Content is ok")
        
    if args is None:
      printc("No arguments found")
      return 404
      exit()
    else:
      printc("Arguments are ok")
    name=content.format(name=name)
    for arg in args:
      txt=content.format(arg=arg)  # If content is test {arg1} {arg2} it will output test {arg1} {arg2}
      # <command> {arg1} {arg2}
      return " ".join([name,txt])
