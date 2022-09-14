# Aingae-Stress
Python code for a GSC account of verbal stress in Aingae

The file "learning_Aingae_stress_with_EDGAR.py" is code for a learning algorithm that learns weights and activations for relevant examples to derive Aingae verbal stress patterns in the Gradient Symbolic Computation framework. The algorithm is similar to the one I developed for learning a model of French Liaison (2019. Learning a model of gradient French liaison (with Paul Smolensky and Matthew Goldrick). Proceedings of the Annual Meeting on Phonology, Stony Brook University, October 2019)

The data analysed come from Maksymilian Dabkowski. 2021. Dominance is non-representational: evidence from A’ingae verbal stress. Phonology 38: 611–650.

Also included are spreadsheets in LibreOfficeCalc and also exported from LOC to excel (I'm not sure how well it exported) which show tableaux for the examples learned by the Python file.

The essentials of the analysis are as follows. Morphemes are abbreviated as A=accented stem, U=unaccented stem, N=recessive "stressless" suffix, S=dominant "stressless" suffix, R=recessive prestressing suffix and D=dominant prestressing suffix. Stress is derived by where a binary head Foot surfaces. Underlying Foot edges are posited as a left Foot edge on an accented stem, left and right Foot edges on a dominant "stressless" suffix, and right Foot edges on recessive and dominant prestressing suffixes. The different behaviour of different morphemes is due to differing degrees of input activation on their input Foot edges.

Relevant weighted constraints are Max/Dep (Path) Left/Right Foot edge. A path constraint requires that input and output Foot edges correspond in position but non-path constraints do not care EXCEPT that I posit a highly-weighted crisp-edge or RightAnchor constraint on stems that prevent a stem's Foot edge from surfacing in the suffix domain and vice versa.

The different behaviour of recessive and dominant prestressing suffixes if due to a weaker input activation on the right Foot edge of R than on D.

The tendency of prestressing to fall before the leftmost prestressing suffix is due to a constraint that requires an input right Foot edge to surface, but it is evaluated locally: only when it falls in a Foot.
