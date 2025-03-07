def get_placeholder_text(conversion_format):
	placeholder_text4input = "Enter text..." if conversion_format.split()[0].startswith("C") else f"Enter {conversion_format.split()[0]}..."
	placeholder_text4output = "Output in Binary..." if conversion_format.split()[0].startswith("C") else f"Output in {conversion_format.split()[2]}..."
	return {"input": placeholder_text4input, "output": placeholder_text4output}