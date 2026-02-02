<!-- 
███████╗██████╗  ██████╗ ███╗   ██╗██╗████████╗    ██╗  ██╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔═══██╗████╗  ██║██║╚══██╔══╝    ██║  ██║██╔════╝╚██╗ ██╔╝
█████╗  ██████╔╝██║   ██║██╔██╗ ██║██║   ██║       ███████║█████╗   ╚████╔╝ 
██╔══╝  ██╔══██╗██║   ██║██║╚██╗██║██║   ██║       ██╔══██║██╔══╝    ╚██╔╝  
███████╗██║  ██║╚██████╔╝██║ ╚████║██║   ██║       ██║  ██║███████╗   ██║   
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝       ╚═╝  ╚═╝╚══════╝   ╚═╝   
-->

<div align="center">

  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3500&pause=800&color=00FFC6&center=true&vCenter=true&width=700&lines=Ethical+Hacking+Toolkit;Botnets+%7C+Cryptography+%7C+L2+Attacks;Scanning+%7C+TCP+Shells;For+Education+Only" alt="Typing SVG" />

  <br>
  <p>🔐 Open-source security tools for research, pentesting & learning — built with Python on Linux.</p>

</div>

---

### ⚠️ Disclaimer

All tools in this repository are intended **strictly for educational purposes and authorized penetration testing**.  
Use responsibly. Unauthorized use is illegal.

---

### 📁 Repository Structure

#### 🤖 **Botnet**
Simulated botnet architecture for understanding C2 communication.
- `botServer.py` – Command-and-control (C2) server that sends instructions to bots.
- `client.py` – Bot client that connects to the C2 server and executes commands.
- `commands.txt` – Example command list sent from server to clients.

#### 🔐 **Cryptography / Ciphers**
Basic classical and symmetric ciphers for educational crypto analysis.
- `caesar.py` – Implements Caesar cipher (shift-based substitution).
- `rot13.py` – ROT13 encoder/decoder (a special case of Caesar cipher).
- `xorCipher.py` – XOR-based encryption/decryption with byte-level support.

#### ⚡ **L2 Attacks** → *ARP Spoofing*
Tools targeting Layer 2 (Data Link) vulnerabilities in local networks.
- `arpSpoof.py` – Performs ARP spoofing to redirect traffic (MITM prep).
- `arpDetector.py` – Monitors ARP table changes to detect spoofing attempts.
- `macFlooding.py` – Simulates MAC flooding attack against switches (educational only).

#### 🔍 **Scanning**
Custom TCP-based port scanning techniques.
- `synScan.py` – Half-open SYN scanner (stealthy, doesn’t complete TCP handshake).
- `xmasScan.py` – Xmas scan using FIN+PSH+URG flags to probe ports.

#### 💀 **TCP Shells**
Reverse and bind shell implementations over raw TCP sockets.
- `reverseShell.py` – Client-side reverse shell that connects back to an attacker.
- `serverShell.py` – Listener that accepts incoming shell connections (used with reverse shell).

---

### ▶️ Quick Start

1. Clone the repo:
   ```bash
   git clone https://github.com/DeltaOpenSource/ethical-hacking.git
   cd ethical-hacking




<h1>Almost all of the code in this repository is the result of learning from Daniel Graham's book on ethical hacking. The code is not the work of DeltaOpenSource!!!</h1>

<h2>All the code in this repository was written by Daniel Graham</h2>
