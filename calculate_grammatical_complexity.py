import csv, sys
from google.cloud import language
client = language.Client()

def calculate_gc(text):
    document = client.document_from_text(text)
    annotations = document.annotate_text()

    root_edge_index = -1
    for token in annotations.tokens:
        if token.edge_label == "ROOT":
            root_edge_index = token.edge_index

    traces = []

    NOUN = 0
    ADJ = 0
    VERB = 0
    ADP = 0
    CONJ = 0

    for token in annotations.tokens:
        edge_index = token.edge_index
        trace = []
        trace.append(edge_index)
        while edge_index is not root_edge_index:
            edge_index = annotations.tokens[edge_index].edge_index
            trace.append(edge_index)

        traces.append(trace)

        if token.part_of_speech == 'NOUN':
            NOUN = NOUN + 1

        if token.part_of_speech == 'ADJ':
            ADJ = ADJ + 1

        if token.part_of_speech == 'VERB':
            VERB = VERB + 1

        if token.part_of_speech == 'ADP':
            ADP = ADP + 1

        if token.part_of_speech == 'CONJ':
            CONJ = CONJ + 1



    max_route = 0
    for trace in traces:
        if len(trace) > max_route:
            max_route = len(trace)

    max_route = max_route + 1

    row = {
        "height": max_route,
        "noun": NOUN,
        "adj": ADJ,
        "verb": VERB,
        "adp": ADP,
        "conj": CONJ
    }

    return row


def calculate_grammatical_complexity(input_filename):
    if input_filename.split(".")[-1] != "csv":
        print ("Input file is not a csv file.")
        return

    results = []

    with open(input_filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            result = row

            gc = calculate_gc(row['english'])
            
            result['noun'] = gc['noun']
            result['adj'] = gc['adj']
            result['verb'] = gc['verb']
            result['adp'] = gc['adp']
            result['conj'] = gc['conj']
            result['height_of_parse_tree'] = gc['height']

            results.append(result)

    filename = input_filename.split('/')[-1].split('.')[0]

    output_filename = 'result/' + filename +  '.csv'
    with open(output_filename, 'w') as csvfile:
        fieldnames = ['english', 'spanish', 'translated_spanish', 'ribes_score', 'number_of_words', 'number_of_alphabets', 'noun', "adj", "verb", "adp", "conj", "height_of_parse_tree"]
        writer =  csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for corpus in results:
            writer.writerow(corpus)


if __name__ == '__main__':
    calculate_features(sys.argv[1])
