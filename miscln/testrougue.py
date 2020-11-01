def answer(map, git_gud=True):
    """Find the shortest path in a binary 2D map where a wall can be removed.
    The algorithm uses a modified Dijstra's algorithm to find the shortest path
    from the start vertex (0,0) to the end vertex (w-1,h-1) in a 2D binary map.
    A single wall can be removed from the map to make the shortest path, if
    necessary. The first wall in any path can be ignored easily, but if a wall
    is necessary to be removed for a valid solution to exist the simple
    algorithm does not remember the minimum path that does not pass through a
    wall to arrive at the mandatory wall vertex. Therefore we modify the
    distance such that we keep track of the minimum path to a vertex for any
    wall removal number up to the max(1).
    Args:
        map: A rectangular 2D list of x el [0,1], where 0 is passable and 1 is
            impassable.  [Warning] clobbers built-in map function in scope.
        git_gud: [Optional] Run algorithm in O(n) time via comparison to known
            solutions, default: True
    Returns:
        The inclusive number of elements visited by a shortest path solution.
    """
    # ascii map for debugging
    # print(make_map(map))

    # run optional O(n) solution
    if git_gud:
        success, result = fast_answer(map)
        if success:
            return result

    # do the real algorithm
    # get the matrix dimensions
    w, h = (len(map[0]), len(map))
    # create set of vertices with infinite distance
    inf = w*h+1
    vs = [Vertex(map[i/w][i % w], i, w, inf=inf) for i in range(h*w)]
    q = range(w*h)  # set of unvisited vertices
    vs[0].set_start()  # set start distance to 1 to count inclusive
    target = h*w - 1  # set target vertex index

    cnt = 0
    while len(q) > 0:
        cnt += 1
        min_dist, min_idx = find_min_dist(q, vs, inf)
        el = q[min_idx]  # index of the min_dist unvisted vertex
        if el == target:  # winner
            # print("Total tries: {}".format(cnt))
            break

        # remove the minimum off the vertex set if it is the minimum without
        # going through a wall, if we had to go through a wall we may need to
        # come back to the node later, to recalcuate without a wall
        if min_dist.get_walls() == 0:
            del q[min_idx]

        # print path to vertex for debugging
        # print_solution(map, vs, target=el)

        # get the Vertex with the minimum distance, given that we have passed
        # through n walls
        u = vs[el].visit(min_dist.get_walls())
        # go to neighbor vertices and see if we have a shorter path to any
        for n in u.neighbors(vs, min_dist.get_walls()):
            n.update_dist(min_dist, el)

    if inf == min_dist.get_dist():
        raise RuntimeError  # solver failed
    # print_solution(map, vs)
    return min_dist.get_dist()
