#! usr/bin/env python
import re

class CssToSassConverter:

	def convert (self, css):
		selectors = self.getSelectors(css);
		statementBlocks = self.getStatementBlocks(css)

		SASS = self.buildSass(selectors, statementBlocks)

		return SASS

	def __getNtabs(self, n):
		tabs = ''
		for ($i = $n; $i > 0; $i--) {
			$tabs = $tabs . "    "
		}
		return tabs

	def __buildSass(self, selectors, statementBlocks, sass = '', originalSelectorString = '', level = 0):
		
		foreach($selectors as $selector => $children):
			selectorString = originalSelectorString + ' ' + selector
			
			$SASS = $SASS . "\n\n" . $this->getNtabs(level) + selector + ' {\n'
			$css = $this->getCssForThisSelector($statementBlocks, $selectorString);
			if (strlen($css) > 0):
				$css = $this->getNtabs($level + 1) . str_replace("\n", "\n" . $this->getNtabs($level + 1), $css)

			SASS = SASS + css

			if (children.count() > 0):
				SASS = $this->buildSass($children, $statementBlocks, $SASS, $selectorString, ($level + 1));
				SASS = $SASS + "\n" . self.getNtabs($level) + "}"
			else:
				SASS = $SASS + "\n" . self.getNtabs($level) + "}"

		return SASS

	def __getCssForThisSelector(statementBlocks, selectorString):
		selectorString = selectorString.strip()
		css = ''

		for( block in statementBlocks) {
			preg_match_all('/\s*' . $selectorString . '\s*{([^}]*)/im', $block, $tmp);

			if (count($tmp[1]) > 0) {
				// mutliple blocks applying to the same selector, need to separate them
				if ($css !== '') {
					$css = $css . "\n";
				}
				$css = $css . trim($tmp[1][0]);	
			}
		}

		return $css;
	}

	def getStatementBlocks (css):
		re.match('/([0-9a-zA-Z#: \.\-_]+{([^}]*))/im', css, statementBlocks)
		for ($i = 0; $i < count($statementBlocks[0]); $i++) {
			$statementBlocks[0][$i] = $statementBlocks[0][$i] . '}';
		}
		$statementBlocks = $statementBlocks[0];
		// trim each line
		for($i = 0; $i < count($statementBlocks); $i++) {
			$statementBlocks[$i] = implode("\n", array_map('trim', explode("\n", $statementBlocks[$i])));
		}
		return statementBlocks

	def getSelectors (self, css):
		re.match('/([0-9a-zA-Z#: \.\-_]+){[^}]*/im', css, self.selectors)
		selectors = self.selectors[1];

		# remove whitespace from the ends
		for($i = 0; $i < count($selectors); $i++) {
			$selectors[$i] = trim($selectors[$i]);
		}

		selectorsToReturn = self.convertSelectorsToNestedArray(selectors)

		return selectorsToReturn

	'''
	Convert
		array(
			".foo .bar",
			".foo .bar p",
			".foo h1"
		)
	to
		array(
			"foo" => array(
				"bar" => array(
					"p" => array()
				),
				"h1" => array()
			)
		)
	'''
	def __convertSelectorsToNestedArray (self, selectors):

		$nestedArray = array();

		for ($i = 0; $i < count($selectors); $i++) {
			$selectorChunks = explode(" ", $selectors[$i]);
			$tmpArray = &$nestedArray;

			foreach ($selectorChunks as $chunk) {

				// if chunk contains ':' character
					// if parent selector exists at this level
						// rename this to &:... and make it a child of that
					// else
						// assume we only ever want to target the : modifier, so just make it its own array

				// @TODO - we should reorder selectors before passing to this function, so that
				// top level selectors come first (i.e. h1, p, etc) and nested selectors come lower,
				// with modifier (':') selectors coming last.
				// otherwise the above pseudocode will not work - you could have a block
				// .something:last-child
				// followed by a block
				// .something
				// and it would be too late - the compiler will have assumed that :last-child was the only
				// modifier of .something we want to target.
				// would be pointless for the compiler to output:
				'''
					.something {
						
						&:last-child {
							// something
						}

					}
				'''

				if (!$tmpArray[$chunk]) {
					$tmpArray[$chunk] = array();
				}
				$tmpArray = &$tmpArray[$chunk];
			}
			unset($tmpArray);
		}

		return nestedArray

