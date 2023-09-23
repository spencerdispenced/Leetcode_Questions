
const hasPath = (graph, src, dst) => {
    // DFS using Recursion
    if (src === dst) return true;

    for (let neighbor of graph[src]) {
         if (hasPath(graph, neighbor, dst)) {
            return true;
         }
    }

    return false;
}



const hasPath_bfs = (graph, src, dst) => {
    // Iterative, cannot use recursion
    const queue = [ src ];

    while (queue.length > 0) {
        const current = queue.shift();  // move the front of queue

        if (current === dst) return true;

        for (let neighbor of graph[current]) {
            queue.push(neighbor)
        }
    }

    return false;
}










const graph = {
    f: ['g', 'i'],
    g: ['h'],
    h: [],
    i: ['g', 'k'],
    j: ['i'],
    k: []
};


console.log(hasPath(graph, 'f', 'k'));  // true
console.log(hasPath_bfs(graph, 'f', 'k'));  // true