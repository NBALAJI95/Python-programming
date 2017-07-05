def main():
    # input given in instructions (list of dictionaries)
    input_val = [{'course': 'python', 'LastGPA' : 90, 'CurrentGPA' : 80},
            {'course': 'python', 'LastGPA' : 95, 'CurrentGPA': 85},
            {'course': 'python', 'LastGPA' : 100, 'CurrentGPA': 100}]

    # Final output list of dictionaries
    final_val = list()

    # looping through each dictionary in the list
    for d in input_val:
        output_val = dict()
        k_v = ''
        v_v = 0
        count = 0
        # looping through each key of the dictionary
        for i in d.keys():
            v = d[i]
            # if value of the key is a digit then add the value else just store
            if str(v).isdigit():
                v_v += v
                if k_v != '':
                    k_v += '+' + i
                else:
                    k_v += i
                count += 1
            else:
                output_val[i] = v
        # Finally storing average
        output_val[k_v] = v_v / count
        # Pushing the dictionary to the end of the list
        final_val.append(output_val)
    print(final_val)

if __name__ == '__main__':
    main()
