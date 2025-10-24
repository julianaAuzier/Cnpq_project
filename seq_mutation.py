#id: identificador do dado
#seq: sequencia
#position: posição a ser alterada
#char: caractere a adicionar/trocar na posição indicada
#mutation: string de mutação. ex.: L293C

def find_mut(id_, seq, mut):
    seq = list(seq.strip())
    old = mut[0] #primeiro caractere sendo sempre 1 letra
    new = mut[-1] #último caractere sendo sempre 1 letra
    position = int(mut[1:-1]) #o que esta entre os caracteres

    print(f'{id_}\n{mut}\nseq_position:{seq[position]}')
    seq[position] = new
    return ''.join(seq)

#ex.:

id_ = 'ACT-89 (P99)'
mutation = 'L293P'
sequence = 'MMRKSLCCALLLGISCSALATPVSEKQLAEVVANTITPLMKAQSVPGMAVAVIYQGKPHYYTFGKADIAANKPVTPQTLFELGSISKTFTGVLGGDAIARGEISLDDAVTRYWPQLTGKQWQGIRMLDLATYTAGGLPLQVPDEVTDNASLLRFYQNWQPQWKPGTTRLYANASIGLFGALAVKPSGMPYEQAMTTRVLKPLKLDHTWINVPKAEEAHYAWGYRDGKAVRVSPGMLDAQAYGVKTNVQDMANWVMANMAPENVADASLKQGIALAQSRYWRIGSMYQGLGWEMLNWPVEANTVVEGSDSKVALAPLPVAEVNPPAPPVKASWVHKTGSTGGFGSYVAFIPEKQIGIVMLANTSYPNPARVEAAYHILEALQ'

seq_mut = find_mut(id_, sequence, mutation)
print(seq_mut)