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
	parsed_results = {query_results['name']: query_results['fql_result_set'] for query_results in multiquery_results['data']}
	print_multiquery_results_information(parsed_results)
	return parsed_results

def parse_and_combine_multiquery_results(multiquery_results):
	"""
	Returns a combined list of all results across all queries of an FQL multiquery.
	"""
	return combine_sublists(parse_multiquery_results(multiquery_results).values())

def random_chunks(full_list, chunk_size):
	"""
	Given a list, returns random disjoint sublists (chunks), each of specified size.
	"""
	shuffle(full_list)
	return [full_list[index:index + chunk_size] for index in xrange(0, len(full_list), chunk_size)]

def combine_sublists(sublists):
	"""
	Given a list of sublists, returns a flattened list.
	"""
	return list(chain.from_iterable(sublists))

def graph_density(node_count, edge_count):
	"""
	Returns the density of a graph with given node and edge counts.
	"""
	return float(edge_count) / edge_count_in_complete_graph(node_count)

def edge_count_in_complete_graph(node_count):
	"""
	Returns the number of edges in a complete graph on a given number of nodes.
	"""
	return node_count * (node_count - 1) / 2

def print_graph_density(node_count, edge_count):
	"""
	Outputs the density of a graph with given node and edge counts.
	"""
	print('\n[GRAPH DENSITY]\t\t' + str(edge_count) + ' of ' + str(edge_count_in_complete_graph(node_count)) + ' (' + str('%.1f' % (100 * graph_density(node_count, edge_count))) + '%) possible edges')

def print_multiquery_results_information(parsed_multiquery_results):
	"""
	Given a dictionary of FQL multiquery results parsed by parse_multiquery_results(),
	oututs each query's name and results count.
	"""
	print('\n[MULTIQUERY RESULTS]')
	for query_name, result in parsed_multiquery_results.iteritems():
		print('\t' + query_name + ':\t' + str(len(result)) + ' results')

def print_friend_chunks_information(friend_chunks):
	"""
	Outputs the number and size of given chunks/sublists of friends.
	"""
	print('\n[FRIEND CHUNKS]\t\t' + str(len(combine_sublists(friend_chunks))) + ' friends in ' + str(len(friend_chunks)) + ' chunks of size ' + str(len(friend_chunks[0])))

def print_execution_time(operation_name, start_time, end_time):
	"""
	Outputs the time an operation took to perform.
	"""
	print('\n[EXECUTION TIME]\t' + operation_name.capitalize() + ' took ' + str('%.1f' % (end_time - start_time)) + ' seconds')

def print_variable_type(variable_name, variable):
	"""
	Outputs the object type (class) of a variable.
	"""
	print '\n[VARIABLE TYPE]\t' + variable_name + ' is a ' + str(type(variable))

def test_and_print_edge_uniqueness(graph):
	"""
	Given a graph, outputs the number of duplicate edges (u,v) <-> (u,v).
	"""
	edge_set = set(graph.edges())
	duplicate_edges = [(edge[0], edge[1]) for edge in graph.edges() if (edge[1], edge[0]) in edge_set]
	print('\n[EDGE UNIQUENESS TEST]\t' + (str(len(duplicate_edges)) + ' duplicate edges detected.' if duplicate_edges else 'No duplicate edges detected.'))



