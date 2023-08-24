import requests
import json

ooba_dict = {
	'auto_max_new_tokens': False,

	# Generation params. If 'preset' is set to different than 'None', the values
	# in presets/preset-name.yaml are used instead of the individual numbers.
	'preset': 'None',
	'do_sample': True,
	'temperature': 0.7,
	'top_p': 0.1,
	'typical_p': 1,
	'epsilon_cutoff': 0,  # In units of 1e-4
	'eta_cutoff': 0,  # In units of 1e-4
	'tfs': 1,
	'top_a': 0,
	'repetition_penalty': 1.18,
	'repetition_penalty_range': 0,
	'top_k': 40,
	'min_length': 0,
	'no_repeat_ngram_size': 0,
	'num_beams': 1,
	'penalty_alpha': 0,
	'length_penalty': 1,
	'early_stopping': False,
	'mirostat_mode': 0,
	'mirostat_tau': 5,
	'mirostat_eta': 0.1,
	'guidance_scale': 1,
	'negative_prompt': '',

	'seed': -1,
	'add_bos_token': True,
	'truncation_length': 2048,
	'ban_eos_token': False,
	'skip_special_tokens': True,
	'stopping_strings': []
	}

def format_prompt_request(gpu_server_addr, id_token, text_prompt, num_tokens):
	# URI = f'http://{gpu_server_addr}/api/v1/generate'
	URI = f'http://{gpu_server_addr}/auth'
	ooba_dict['prompt'] = text_prompt
	ooba_dict['max_new_tokens'] = num_tokens
	request_dict = {"token" : id_token, "ooba" : ooba_dict}
	text_result = None
	error = None
	try:
		response = requests.post(URI, json=request_dict)
		if response.status_code == 200:
			try:
				result = response.json()['results'][0]['text']
				text_result = text_prompt + result
			except json.decoder.JSONDecodeError:
				error = "json"
		else:
			error = f"code:{response.status_code}"
	except requests.exceptions.ConnectionError as e:
		error = f"connection error:{e}"

	return {"reply" : text_result, "error": error}

def main():
	pass
	# addr = "195.29.196.251:50011"
	# regular_prompt = "What is your name?"
	# response = format_prompt_request(addr, regular_prompt, 200)
	# print(response)

if __name__ == "__main__":
	main()