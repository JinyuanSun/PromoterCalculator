from promoter_calculator import Promoter_Calculator

test_seq_0 = "GACAAGTTGTCAGTTATCTCTTCGGATATTTGTCTATTTCGTCCGAAATATTGTCAGTCGAACTCGGGTGAATACGTTTGGCACACTATTCGCATAGACTTAGGCGTGAACACAAAGTTCATAAACTAAAAACGTAATATTATTAACATTTAAAATACCAAGAAA"

calc = Promoter_Calculator()

def process_sequence(sequence):
    calc.run(sequence, TSS_range=[60, len(sequence)])
    output = calc.output()
    score_list = [result['Tx_rate'] for result in output['Forward_Predictions_per_TSS'].values()]
    # print(sequence, score_list)
    index = score_list.index(max(score_list))
    core_promoter = sequence[index:index + 60]
    return sequence, core_promoter, max(score_list)

sequence, core_promoter, score = process_sequence(test_seq_0)

print("Input sequence:\n" + test_seq_0)
print("Core promoter sequence:\n" + core_promoter)
print("Predicted score:\n" + str(score))