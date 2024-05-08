greek_text = "Σὲ γνωρίζω ἀπὸ τὴν κόψη"
print(greek_text.casefold())  # Output: σὲ γνωρίζω ἀπὸ τὴν κόψη
print(greek_text.lower())     # Output: σὲ γνωρίζω ἀπὸ τὴν κόψη

# casefold will handle all kinds of text
german_text = "Straßenbahn"
print(german_text.casefold())  # Output: strassebahn
print(german_text.lower())     # Output: straßenbahn