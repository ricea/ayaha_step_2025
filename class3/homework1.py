#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def read_times(line, index):
    token = {'type': 'TIMES'}
    return token, index + 1

def read_slash(line, index):
    token = {'type': 'SLASH'}
    return token, index + 1

def read_open_paren(line, index):
    token = {'type': 'OPEN_PAREN'}
    return token, index + 1

def read_close_paren(line, index):
    token = {'type': 'CLOSE_PAREN'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_times(line, index)
        elif line[index] == '/':
            (token, index) = read_slash(line, index)
        elif line[index] == '(':
            (token, index) = read_open_paren(line, index)
        elif line[index] == ')':
            (token, index) = read_close_paren(line, index)       
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def evaluate_without_parens(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    # 積・商の計算
    index = 1 
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'TIMES':
                tokens[index-2]['number'] = tokens[index-2]['number'] * tokens[index]['number']
                del tokens[index-1:index+1]
                index -= 2   
            elif tokens[index - 1]['type'] == 'SLASH':
                tokens[index-2]['number'] = tokens[index-2]['number'] / tokens[index]['number']
                del tokens[index-1:index+1]
                index -= 2
        index += 1 
    # 和・差の計算
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer

def evaluate_total(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'})
    # 括弧の内部の値を計算する
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'CLOSE_PAREN':
            # )に対応する()内の値を計算
            open_parens_index = 0
            for i in range(index, -1, -1):
                if tokens[i]['type'] == 'OPEN_PAREN':
                    open_parens_index = i
                    break
            part_of_tokens = tokens[open_parens_index+1:index] 
            del tokens[open_parens_index:index+1]
            tokens.insert(open_parens_index, {'type': 'NUMBER', 'number': evaluate_without_parens(part_of_tokens)})
            index = open_parens_index + 1
        else:
            index += 1
    # 括弧が全てはずれた式を計算する
    return evaluate_without_parens(tokens)
            

def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate_total(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1")
    test("1+2")
    test("1.0+2")
    test("1.0+2.0")
    test("1.0+2.1-3")
    test("2*3")
    test("2.5*4/7")
    test("3*4+5")
    test("1-2/4+3*5")
    test("(2-1)")
    test("(2-1)*4")
    test("3.0+4*(2-1)")
    test("((2-1)*5)")
    test("(3.0+4*(2-1))/5")
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate_total(tokens)
    print("answer = %f\n" % answer)