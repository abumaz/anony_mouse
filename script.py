from selenium import webdriver
import random
n = int(input("Enter the number of times you want to submit a response: "))
names=['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Charlotte', 'Mia', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Mila', 'Ella', 'Avery', 'Sofia', 'Camila', 'Aria', 'Scarlett', 'Victoria', 'Madison', 'Luna', 'Grace', 'Chloe', 'Penelope', 'Layla', 'Riley', 'Zoey', 'Nora', 'Lily', 'Eleanor', 'Hannah', 'Lillian', 'Addison', 'Aubrey', 'Ellie', 'Stella', 'Natalie', 'Zoe', 'Leah', 'Hazel', 'Violet', 'Aurora', 'Savannah', 'Audrey', 'Brooklyn', 'Bella', 'Claire', 'Skylar', 'Lucy', 'Paisley', 'Everly', 'Anna', 'Caroline', 'Nova', 'Genesis', 'Emilia', 'Kennedy', 'Samantha', 'Maya', 'Willow', 'Kinsley', 'Naomi', 'Aaliyah', 'Elena', 'Sarah', 'Ariana', 'Allison', 'Gabriella', 'Alice', 'Madelyn', 'Cora', 'Ruby', 'Eva', 'Serenity', 'Autumn', 'Adeline', 'Hailey', 'Gianna', 'Valentina', 'Isla', 'Eliana', 'Quinn', 'Nevaeh', 'Ivy', 'Sadie', 'Piper', 'Lydia', 'Alexa', 'Josephine', 'Emery', 'Julia', 'Delilah', 'Arianna', 'Vivian', 'Kaylee', 'Sophie', 'Brielle', 'Madeline', 'Peyton', 'Rylee', 'Clara', 'Hadley', 'Melanie', 'Mackenzie', 'Reagan', 'Adalynn', 'Liliana', 'Aubree', 'Jade', 'Katherine', 'Isabelle', 'Natalia', 'Raelynn', 'Maria', 'Athena', 'Ximena', 'Arya', 'Leilani', 'Taylor', 'Faith', 'Rose', 'Kylie', 'Alexandra', 'Mary', 'Margaret', 'Lyla', 'Ashley', 'Amaya', 'Eliza', 'Brianna', 'Bailey', 'Andrea', 'Khloe', 'Jasmine', 'Melody', 'Iris', 'Isabel', 'Norah', 'Annabelle', 'Valeria', 'Emerson', 'Adalyn', 'Ryleigh', 'Eden', 'Emersyn', 'Anastasia', 'Kayla', 'Alyssa', 'Juliana', 'Charlie', 'Esther', 'Ariel', 'Cecilia', 'Valerie', 'Alina', 'Molly', 'Reese', 'Aliyah', 'Lilly', 'Parker', 'Finley', 'Morgan', 'Sydney', 'Jordyn', 'Eloise', 'Trinity', 'Daisy', 'Kimberly', 'Lauren', 'Genevieve', 'Sara', 'Arabella', 'Harmony', 'Elise', 'Remi', 'Teagan', 'Alexis', 'London', 'Sloane', 'Laila', 'Lucia', 'Diana', 'Juliette', 'Sienna', 'Elliana', 'Londyn', 'Ayla', 'Callie', 'Gracie', 'Josie', 'Amara', 'Jocelyn', 'Daniela', 'Everleigh', 'Mya', 'Rachel', 'Summer', 'Alana', 'Brooke', 'Alaina', 'Mckenzie', 'Catherine', 'Amy', 'Presley', 'Journee', 'Rosalie', 'Ember', 'Brynlee', 'Rowan', 'Joanna', 'Paige', 'Rebecca', 'Ana', 'Sawyer', 'Mariah', 'Nicole', 'Brooklynn', 'Payton', 'Marley', 'Fiona', 'Georgia', 'Lila', 'Harley', 'Adelyn', 'Alivia', 'Noelle', 'Gemma', 'Vanessa', 'Journey', 'Makayla', 'Angelina', 'Adaline', 'Catalina', 'Alayna', 'Julianna', 'Leila', 'Lola', 'Adriana', 'June', 'Juliet', 'Jayla', 'River', 'Tessa', 'Lia', 'Dakota', 'Delaney', 'Selena', 'Blakely', 'Ada', 'Camille', 'Zara', 'Malia', 'Hope', 'Samara', 'Vera', 'Mckenna', 'Briella', 'Izabella', 'Hayden', 'Raegan', 'Michelle', 'Angela', 'Ruth', 'Freya', 'Kamila', 'Vivienne', 'Aspen', 'Olive', 'Kendall', 'Elaina', 'Thea', 'Kali', 'Destiny', 'Amiyah', 'Evangeline', 'Cali', 'Blake', 'Elsie', 'Juniper', 'Alexandria', 'Myla', 'Ariella', 'Kate', 'Mariana', 'Lilah', 'Charlee', 'Daleyza', 'Nyla', 'Jane', 'Maggie', 'Zuri', 'Aniyah', 'Lucille', 'Leia', 'Melissa', 'Adelaide', 'Amina', 'Giselle', 'Lena', 'Camilla', 'Miriam', 'Millie', 'Brynn', 'Gabrielle', 'Sage', 'Annie', 'Logan', 'Lilliana', 'Haven', 'Jessica', 'Kaia', 'Magnolia', 'Amira', 'Adelynn', 'Makenzie', 'Stephanie', 'Nina', 'Phoebe', 'Arielle', 'Evie', 'Lyric', 'Alessandra', 'Gabriela', 'Paislee', 'Raelyn', 'Madilyn', 'Paris', 'Makenna', 'Kinley', 'Gracelyn', 'Talia', 'Maeve', 'Rylie', 'Kiara', 'Evelynn', 'Brinley', 'Jacqueline', 'Laura', 'Gracelynn', 'Lexi', 'Ariah', 'Fatima', 'Jennifer', 'Kehlani', 'Alani', 'Ariyah', 'Luciana', 'Allie', 'Heidi', 'Maci', 'Phoenix', 'Felicity', 'Joy', 'Kenzie', 'Veronica', 'Margot', 'Addilyn', 'Lana', 'Cassidy', 'Remington', 'Saylor', 'Ryan', 'Keira', 'Harlow', 'Miranda', 'Angel', 'Amanda', 'Daniella', 'Royalty', 'Gwendolyn', 'Ophelia', 'Heaven', 'Jordan', 'Madeleine', 'Esmeralda', 'Kira', 'Miracle', 'Elle', 'Amari', 'Danielle', 'Daphne', 'Willa', 'Haley', 'Gia', 'Kaitlyn', 'Oakley', 'Kailani', 'Winter', 'Alicia', 'Serena', 'Nadia', 'Aviana', 'Demi', 'Jada', 'Braelynn', 'Dylan', 'Ainsley', 'Alison', 'Camryn', 'Avianna', 'Bianca', 'Skyler', 'Scarlet', 'Maddison', 'Nylah', 'Sarai', 'Regina', 'Dahlia', 'Nayeli', 'Raven', 'Helen', 'Adrianna', 'Averie', 'Skye', 'Kelsey', 'Tatum', 'Kensley', 'Maliyah', 'Erin', 'Viviana', 'Jenna', 'Anaya', 'Carolina', 'Shelby', 'Sabrina', 'Mikayla', 'Annalise', 'Octavia', 'Lennon', 'Blair', 'Carmen', 'Yaretzi', 'Kennedi', 'Mabel', 'Zariah', 'Kyla', 'Christina', 'Selah', 'Celeste', 'Eve', 'Mckinley', 'Milani', 'Frances', 'Jimena', 'Kylee', 'Leighton', 'Katie', 'Aitana', 'Kayleigh', 'Sierra', 'Kathryn', 'Rosemary', 'Jolene', 'Alondra', 'Elisa', 'Helena', 'Charleigh', 'Hallie', 'Lainey', 'Avah', 'Jazlyn', 'Kamryn', 'Mira', 'Cheyenne', 'Francesca', 'Antonella', 'Wren', 'Chelsea', 'Amber', 'Emory', 'Lorelei', 'Nia', 'Abby', 'April', 'Emelia', 'Carter', 'Aylin', 'Cataleya', 'Bethany', 'Marlee', 'Carly', 'Kaylani', 'Emely', 'Liana', 'Madelynn', 'Cadence', 'Matilda', 'Sylvia', 'Myra', 'Fernanda', 'Oaklyn', 'Elianna', 'Hattie', 'Dayana', 'Kendra', 'Maisie', 'Malaysia', 'Kara']
br=webdriver.Firefox()
for i in range(n):
	print('Response no:'+str(i+1))
	br.get("https://docs.google.com/forms/d/e/1FAIpQLSfwIhD0CPYl2TlYO9P5zUA0DpzYWYXKv076ilWV1CAfVsYGtA/viewform")
	name=names[random.randint(0,500)-1]
	elem=br.find_element_by_css_selector('.freebirdFormviewerComponentsQuestionTextShort > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
	elem.send_keys(name)
	elem2=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)')
	elem2.click()
	choice=random.randint(0,4)
	if choice == 1:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerComponentsQuestionCheckboxChoice:nth-child(1) > label:nth-child(1)')
		elem3.click()
	elif choice == 2:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerComponentsQuestionCheckboxChoice:nth-child(2) > label:nth-child(1)')
		elem3.click()
	elif choice == 3:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerComponentsQuestionCheckboxChoice:nth-child(3) > label:nth-child(1)')
		elem3.click()
	else:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerComponentsQuestionCheckboxChoice:nth-child(4) > label:nth-child(1)')
		elem3.click()
	choice=random.randint(0,3)
	if choice == 1:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)')
		elem3.click()
	elif choice == 2:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1)')
		elem3.click()
	else:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1)')
		elem3.click()
	choice=random.randint(0,3)
	if choice == 1:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)')
		elem3.click()
	elif choice == 2:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1)')
		elem3.click()
	else:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1)')
		elem3.click()
	choice=random.randint(0,3)
	if choice == 1:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)')
		elem3.click()
	elif choice == 2:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1)')
		elem3.click()
	else:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1)')
		elem3.click()
	choice=random.randint(0,3)
	if choice == 1:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)')
		elem3.click()
	elif choice == 2:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1)')
		elem3.click()
	else:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1)')
		elem3.click()
	choice=random.randint(0,4)
	if choice == 1:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)')
		elem3.click()
	elif choice == 2:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1)')
		elem3.click()
	elif choice == 3:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1)')
		elem3.click()
	else:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(4) > label:nth-child(1)')
		elem3.click()
	choice=random.randint(0,4)
	if choice == 1:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)')
		elem3.click()
	elif choice == 2:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1)')
		elem3.click()
	elif choice == 3:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1)')
		elem3.click()
	else:
		elem3=br.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(4) > label:nth-child(1)')
		elem3.click()
	choice=random.randint(0,24)-1
	elem=br.find_element_by_css_selector('div.quantumWizTextinputPaperinputEl:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
	elem.send_keys(choice)
	choice=random.randint(0,61)-1
	elem=br.find_element_by_css_selector('div.freebirdFormviewerComponentsQuestionTimeTimeInput:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
	elem.send_keys(choice)

	sub=br.find_element_by_css_selector('.appsMaterialWizButtonPaperbuttonFilled')
	sub.click()
	br.back()
	print("Sent")
