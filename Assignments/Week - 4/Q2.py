def main():
    input_val = [{'course': 'python', 'LastGPA' : 90, 'CurrentGPA' : 80},
            {'course': 'python', 'LastGPA' : 95, 'CurrentGPA': 85},
            {'course': 'python', 'LastGPA' : 100, 'CurrentGPA': 100}]

    final_val = list()

    for d in input_val:
        output_val = dict()
        k_v = ''
        v_v = 0
        count = 0
        for i in d.keys():
            #print(i)
            v = d[i]
            if str(v).isdigit():
                v_v += v
                if k_v != '':
                    k_v += '+' + i
                else:
                    k_v += i
                count += 1
            else:
                output_val[i] = v
        output_val[k_v] = v_v / count
        final_val.append(output_val)
    print(final_val)

if __name__ == '__main__':
    main()
