def consensus(strings):
    n = len(strings)
    m = len(strings[0])

    freq_dict = {symbol: [0] * m for symbol in 'ACGT'}

    for string in strings:
        for i in range(m):
            freq_dict[string[i]][i] += 1

    consensus = []
    for i in range(m):
        max_symbol = 'A'
        for symbol in 'ACGT':
            if freq_dict[symbol][i] > freq_dict[max_symbol][i]:
                max_symbol = symbol
            elif freq_dict[symbol][i] == freq_dict[max_symbol][i] and symbol < max_symbol:
                max_symbol = symbol
        consensus.append(max_symbol)

    return ''.join(consensus)

strings = ['ATTA', 'ACTA', 'AGCA', 'ACAA']
print(consensus(strings))  # выводит "ACTA"
