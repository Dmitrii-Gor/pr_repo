
class Stack():

    def __init__(self, get_stack):
        self.stack = list(get_stack)

    def is_empty(self):
        if self.stack == []:
            return 'True'
        else:
            return 'False'

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size_of_stack(self):
        return len(self.stack)


def correct_mes(text):
    stack_class_old = Stack(text)
    stack_class_new = Stack([])
    if (stack_class_old.size_of_stack()) % 2 != 0:
        return 'Скобки стоят неверно'
    else:
        while stack_class_old.size_of_stack() > 0:
            if stack_class_old.peek() == ']' or stack_class_old.peek() == '}' or stack_class_old.peek() == ')':
                stack_class_new.push(stack_class_old.pop())
            else:
                stack_final = stack_class_old.pop() + stack_class_new.pop()
                if stack_final == '[]' or stack_final == '{}' or stack_final == '()':
                    continue
                else:
                    return 'Скобки стоят неверно'

        if stack_class_old.size_of_stack() == 0:
            return 'Сбалансированно'

print(correct_mes('(((([{}]))))'))
print(correct_mes('[([])((([[[]]])))]{()}'))
print(correct_mes('{{[()]}}'))
print(correct_mes('}{}'))
print(correct_mes('{{[(])]}}'))
print(correct_mes('[[{())}]'))