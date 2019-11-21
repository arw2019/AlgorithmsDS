# top 10%

from collections import defaultdict
class Solution:
        
    def generateSentences(self, synonym_pairs: List[List[str]], text: str) -> List[str]:
        
        # synonym_pairs defines an undirected graph with words as vertices
        # two verticies are connected if they are synonymous
        
        # load data into an adjacency list(graph)
        adj = defaultdict(list)    
        for word1, word2 in synonym_pairs:
            adj[word1] += [word2]
            adj[word2] += [word1]
        
        # we need the connected components of this undirected graph
        # we use dfs
        
        unseen = set(adj.keys()) # tracks which verticies have been visited
        synonyms = defaultdict(list) # key = group no, value = synonymous words
        assignments = defaultdict(int) # key = word, value = synonomous group
        
        # dfs implementation
        def dfs(word1, i):
            for word2 in adj[word1]:
                if word2 in unseen:
                    unseen.remove(word2)
                    assignments[word2] = i
                    synonyms[i] += [word2]
                    dfs(word2, i)
                
        i = 1
        for key, words in adj.items():
            if key in unseen:
                assignments[key] = i
                dfs(key, i)
                i+=1
            
        # sort each synonomous group so that we generate synonymous text in lexicographic order
        for idx, words in synonyms.items():
            words.sort()
            
        
        text = text.split(' ')
        num_words = len(text)
        
        # we do "bfs" on the text to generate synonymous versions
        queue, i = [text], 0 
        for i, word in enumerate(text):
            group = assignments[word]
            words = synonyms[group]
            if words: 
                queue = [q[:i] + [synonym] + q[i+1:] for q in queue for synonym in words]
        
        return [' '.join(t) for t in queue]