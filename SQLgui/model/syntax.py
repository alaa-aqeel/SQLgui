from . import QSyntaxHighlighter,re,QTextCharFormat,QColor,Qt,QRegExp


class syntax(QSyntaxHighlighter):
	def __init__(self,parent):
		super(syntax,self).__init__(parent)
		self.highlightRules = []
		keyword = QTextCharFormat()
		keyword.setForeground(QColor(200,38,89))
		keywords = open('SQLgui/static/sql_keywords','r').read().strip('#####').split("\n")
		for i in keywords:
			self.highlightRules.append((QRegExp("\\b%s\\b"%i),keyword))

		keyblue = ['BIGINT', 'INTEGER', 'INT', 'SMALLINT', 'BIT', 'DECIMAL', 'NUMERIC', 'MONEY',
		 'REAL', 'DATETIME', 'DATE', 'TIME', 'CHAR()','VARCHAR()', 'TEXT', 'NVARCHAR',
		 'NTEXT', 'VARBINARY', 'bigint', 'int', 'smallint', 'bit', 'decimal', 'numeric',
		 'money','real', 'datetime', 'date', 'time', 'char', 'varchar', 'text', 'nvarchar',
		  'ntext','integer', 'varbinary',"utf8"]
		
		keywordt = QTextCharFormat()
		keywordt.setForeground(QColor(0,162,232))
		for i in keyblue:
			self.highlightRules.append((QRegExp("\\b%s\\b"%i),keywordt))
		
		keyword = QTextCharFormat()
		keyword.setForeground(QColor(Qt.blue))
		self.highlightRules.append((QRegExp(r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b'),keyword))
		quotation = QTextCharFormat()
		quotation.setForeground(QColor(0,144,0))
		regu = r'(\br|u|ur|R|U|UR|Ur|uR|b|B|br|Br|bR|BR|rb|rB|Rb|RB)?'
		self.highlightRules.append((QRegExp(regu+r'"[^"\\\n]*(\\.[^"\\\n]*)*"?'),
		    quotation))
		self.highlightRules.append((QRegExp(regu+r"'[^'\\\n]*(\\.[^'\\\n]*)*'?"),
		    quotation))
		
		
		self.multiLineCommentFormat = QTextCharFormat()
		self.multiLineCommentFormat.setForeground(QColor(117,113,84))
		
		self.commentStartExpression = QRegExp("/\\*")
		self.commentEndExpression = QRegExp("\\*/")
        
		
	def highlightBlock(self,text):
		for pattern, form in self.highlightRules:
			expression = QRegExp(pattern)
			index = expression.indexIn(text)
			while index >= 0:
				length = expression.matchedLength()
				self.setFormat(index, length, form)
				index = expression.indexIn(text, index + length)
				

		self.setCurrentBlockState(0)
		startIndex = 0
		if self.previousBlockState() != 1:
		    startIndex = self.commentStartExpression.indexIn(text)
		
		while startIndex >= 0:
		    endIndex = self.commentEndExpression.indexIn(text, startIndex)
		
		    if endIndex == -1:
		        self.setCurrentBlockState(1)
		        commentLength = len(text) - startIndex
		    else:
		        commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()
		
		    self.setFormat(startIndex, commentLength,
		            self.multiLineCommentFormat)
		    startIndex = self.commentStartExpression.indexIn(text,
		            startIndex + commentLength);
