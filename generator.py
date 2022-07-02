import re
num_range = r"(\[(\d+)-(\d+)\])"  #[1-9]
symboles_range = r"(\[(\W+)+\])"  #[@,#,.]




class Generator:
	def __init__(self, _plugins):
		self.plugins = _plugins
	 
	def run(self, _line, _new_line, idx, plugin_idx):
		_res = []
		# for plugin in self.plugins:
		# _res.extend( self.plugins[0].fill(_line, None, idx))
		p = self.plugins[0].fill(_line, None, 0, self.plugins,0)
		for i in p:
			_res.append(i)
		return _res


class NumbersPlugin:
	def __init__(self, _regex):
		self.regex = _regex
		
	def founds(self,_line):
		return re.findall(self.regex, _line)
	
	def check(self, _line):
		return len( re.findall(self.regex, _line)) > 0
	
	def fill(self, _line, _new_line, idx,plugins,indexPlugin):
		founds = self.founds(_line)
		if _new_line is None:  _new_line = _line
		_res = []
		if len(founds) > idx:
			for s1 in range(int(founds[idx][1]),int(founds[idx][2]) + 1):
				d1 = _new_line.replace(founds[idx][0],str(s1))
				#can we go deeper
				if len(founds) > idx + 1:
					[ _res.append(x) for x in self.fill(_line, d1, idx + 1,plugins,indexPlugin) ]
				else:
						if self.check()
						[ _res.append(x) for x in self.fill(_line, d1, idx + 1,plugins,indexPlugin+1) ]
				_res.append(d1)
		return _res