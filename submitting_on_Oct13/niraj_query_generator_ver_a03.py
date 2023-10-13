



from sentence_transformers import SentenceTransformer, util
import spacy




def generate_niraj_search_queries(
        sentence_model, spacy_model, 
        corpus_file_path = "./Data/corpus.txt", 
        output_file_path = './Data/queries.txt', 
        ):
    # Load LaBSE model
    model = sentence_model
    nlp = spacy_model

    with open(corpus_file_path, 'r') as file:
        corpus = file.read()

    def extract_entities(text, nlp):
        doc = nlp(text)
        named_entities = []
        # product_entities = []
        for ent in doc.ents:
            named_entities.append(ent.text)
        return named_entities
    named_entities = extract_entities(corpus, nlp)
    embeddings1 = model.encode(corpus, convert_to_tensor=True)

    query_scores = []
    entities = []
    for ent in named_entities:
        if ent in entities:
            continue
        temp = []
        # print(ent)
        embeddings2 = model.encode(ent, convert_to_tensor=True)
        similarity_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
        # print(similarity_scores)
        entities.append(ent)
        temp.append(ent)
        temp.append(similarity_scores)
        query_scores.append(temp)

    query_scores.sort(key=lambda x: x[1], reverse=True)
    top_queries = query_scores[:10]
    with open(output_file_path, 'w') as output_file:
        # Write each query to a new line in the file
        for query in top_queries:
            output_file.write(str(query[0]) + '\n')
    queries = [pair[0] for pair in top_queries]
    return queries




