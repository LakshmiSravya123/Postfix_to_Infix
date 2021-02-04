
class PostToIn():

# Get Infix expression for a given postfix expression
  binary_operators = set(['+', '-', '*', '/','=', '<', '>'])#binary operators
  unary_operators=set(['√' ,'!',])#unary operators


  def postfixToInfix(self,formula):
    self.formula=formula
    list=self.formula.split()# splitting the expression in to tokens
    stack = []# empty stack
    pos=-1 #position of token in the lists
    for ch in list:
        pos += 1
        if (not ch in PostToIn.binary_operators) and (not ch in PostToIn.unary_operators):
        #appending in to stack other than operators
            stack.append(ch)
        elif ch in PostToIn.binary_operators:
        #binary operator pop twice
            a=''
            if(len(stack)!=0):
                b = stack.pop()

            if (len(stack) != 0):
                a = stack.pop()

            #if list reaches the end
            if pos == len(list) - 1  :
                expression =  a + ch + b #expression of the stack at the end of the list

            else :
                expression = '('+ a + ch + b+ ')' #expression of the stack
            stack.append(expression)#appending expression with the stack


        elif ch in PostToIn.unary_operators:
        #unary operators pop once
            if (len(stack) != 0):
               c=stack.pop()
               if(ch=='!'):
                   expression=c+ch # operator added at the end of the expression for factorial
               else:
                   expression=ch+c # operator added before the expression for root

            stack.append(expression)

    print (stack[-1])#print the end stack
    return stack[-1]#returning the stack




