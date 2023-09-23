


const depthFirstSearch = (graph, source) => {
    const stack = [source];

    while (stack.length > 0) {
        const current = stack.pop();
        console.log(current);

        for (let neighbor of graph[current]) {
            stack.push(neighbor);
        }
    }
}



const depthFirstSearchRecursive = (graph, source) => {
    console.log(source);
    for (let neighbor of graph[source]) {
        depthFirstSearchRecursive(graph, neighbor);
    }
}



const breadthFirstSearch = (graph, source) => {
    const queue = [ source ];
    while (queue.length > 0) {
        const current = queue.shift();
        console.log(current);

        for (let neighbor of graph[current]) {
            queue.push(neighbor)
        }
    }
}



const graph = {
    a: ['c', 'b'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: []
};

// depthFirstSearch(graph, 'a'); // abdfce or acebdf
// depthFirstSearchRecursive(graph, 'a')
breadthFirstSearch(graph, 'a'); // acbedf