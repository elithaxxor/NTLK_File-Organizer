1. **Scanner**: Files related to scanning tools (e.g., Nmap, Masscan).
2. **Exploitation**: Files concerning exploitation tools (e.g., Metasploit, various exploits).
3. **Web_Tools**: Files associated with web tools (e.g., Burp Suite, DirBuster).
4. **Password_Cracking**: Files linked to password cracking tools (e.g., Hydra, John the Ripper).
5. **Sniffing**: Files involving sniffing tools (e.g., Wireshark, Tcpdump).
6. **Other**: Files that do not belong to any of the above categories.

[[OVERVIEW]]
Machine learning models can be trained using labeled datasets of cybersecurity tools to predict categories like “Scanner,” “Exploitation,” or “Web Tools.” For example:
	•	Tools like Wireshark and Tcpdump can be categorized under “Sniffing.”
	•	Tools like Metasploit and Cobalt Strike fall under “Exploitation”.

[[V1 Change Log]]
 Updates to Training Data:
	1.	Scanner: Added tools like Shodan, TheHarvester.
	2.	Exploitation: Included SQLMap, Cobalt Strike, Empire.
	3.	Web_Tools: Added OWASP ZAP, WPScan.
	4.	Password_Cracking: Expanded with Hashcat, Cain & Abel.
	5.	Sniffing: Added Kismet, Aircrack-ng.
	6.	Encryption: Included VeraCrypt, AxCrypt, Tor, NordLocker.
	7.	Network_Defense: Added Snort, Suricata, pfSense, AlienVault OSSIM.
 
How It Works:
	1.	Categories: Expanded categories now include encryption tools and network defense tools alongside the original ones.
	2.	Training Data: Richer examples ensure better categorization accuracy.
	3.	Classifier: Uses TF-IDF vectorization and Naive Bayes classification.
Steps to Run:
