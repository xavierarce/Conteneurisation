def create_matrix_5x4(default_value=0):
	return [[default_value for _ in range(4)] for _ in range(5)]


def create_matrix(n, m, default_value=0):
	if n <= 0 or m <= 0:
		raise ValueError("Les dimensions doivent être strictement positives")
	return [[default_value for _ in range(m)] for _ in range(n)]


def add_matrices(a, b):
	_check_same_shape(a, b)
	return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def subtract_matrices(a, b):
	_check_same_shape(a, b)
	return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiply_matrices(a, b):
	if len(a[0]) != len(b):
		raise ValueError("Matrices incompatibles pour la multiplication")

	rows = len(a)
	cols = len(b[0])
	common = len(b)
	result = create_matrix(rows, cols, 0)

	for i in range(rows):
		for j in range(cols):
			for k in range(common):
				result[i][j] += a[i][k] * b[k][j]
	return result


def calculate_matrix_operation(op, a, b):
	if op == "+":
		return add_matrices(a, b)
	if op == "-":
		return subtract_matrices(a, b)
	if op in ("x", "*"):
		return multiply_matrices(a, b)
	if op == "/":
		_check_same_shape(a, b)
		return [
			[a[i][j] / b[i][j] if b[i][j] != 0 else 1 for j in range(len(a[0]))]
			for i in range(len(a))
		]
	raise ValueError("Opération non supportée")


def _check_same_shape(a, b):
	if len(a) == 0 or len(b) == 0:
		raise ValueError("Les matrices ne peuvent pas être vides")
	if len(a) != len(b) or len(a[0]) != len(b[0]):
		raise ValueError("Matrices incompatibles")
