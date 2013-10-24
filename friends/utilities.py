"""
utilities.py contains utility functions used throughout the 'friends' app.
"""
from random import shuffle
from itertools import chain

def parse_multiquery_results(multiquery_results):
	"""
	Given the results of an FQL multiquery, returns a dictionary mapping query
	names to a list of results for that query.
	"""
	return {query_results['name']: query_results['fql_result_set'] for query_results in multiquery_results['data']}

def parse_and_combine_multiquery_results(multiquery_results):
	"""
	Given the results of an FQL multiquery, returns a combined list of all results
	across all queries.
	"""
	# return combine_sublists(parse_multiquery_results(multiquery_results).values())
	results = parse_multiquery_results(multiquery_results).values()
	for partial_results in results:
		print(str(len(partial_results)) + ' partial results')
	return combine_sublists(results)

def shuffled_chunks(full_list, chunk_size):
	"""
	Given a list, returns sublists of specified size in a randomized order.
	"""
	shuffle(full_list)
	return [full_list[index:index + chunk_size] for index in xrange(0, len(full_list), chunk_size)]

def combine_sublists(sublists):
	"""
	Given a list of sublists, returns a list containing the items in all sublists (i.e. flattens the list).
	"""
	return list(chain.from_iterable(sublists))

def edge_count_in_complete_graph(node_count):
	"""
	Returns the number of edges in a complete graph on a given number of nodes.
	"""
	return node_count * (node_count - 1) / 2

def print_graph_density(node_count, edge_count):
	"""
	Outputs the density of a graph with the given node and edge counts.
	"""
	print('[GRAPH DENSITY] ' + str(edge_count) + ' out of ' + str(edge_count_in_complete_graph(node_count)) + ' edges exist (' + str('%.1f' % (100 * float(edge_count) / edge_count_in_complete_graph(node_count))) + '%)')

def print_friend_chunks_information(friend_chunks):
	"""
	Outputs the number and size of given chunks/sublists of friends.
	"""
	print('[FRIEND CHUNKS] ' + str(sum([len(chunk) for chunk in friend_chunks])) + ' friends split into ' + str(len(friend_chunks)) + ' chunks of size ' + str(len(friend_chunks[0])))

def print_execution_time(operation_name, start_time, end_time):
	"""
	Outputs the execution time (in seconds) of an operation to the console.
	"""
	print('[EXECUTION TIME] ' + str('%.1f' % (end_time - start_time)) + ' seconds:\t' + operation_name)

def print_variable_type(variable_name, variable):
	"""
	Outputs the object type (class) of a variable.
	"""
	print '[VARIABLE TYPE] ' + variable_name + ' is a ' + str(type(variable))

def test_and_print_edge_uniqueness(graph):
	"""
	Given a graph, outputs the number of duplicate edges (u,v) and (u,v), if any.
	"""
	edge_set = set(graph.edges())
	duplicate_edges = [(edge[0], edge[1]) for edge in graph.edges() if (edge[1], edge[0]) in edge_set]
	print('[EDGE UNIQUENESS TEST] ' + (str(len(duplicate_edges)) + ' duplicate edges detected.' if duplicate_edges else 'No duplicate edges detected.'))



