"""
utilities.py contains utility functions used throughout the 'friends' app.
"""

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
	return [result for query_results in multiquery_results['data'] for result in query_results['fql_result_set']]

def chunks(full_list, chunk_size):
	"""
	Given a list, returns successive sublists of specified size.
	"""
	return [full_list[index:index+chunk_size] for index in xrange(0, len(full_list), chunk_size)]

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



