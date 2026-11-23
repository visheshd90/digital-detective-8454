# Mission 7 - Networks and the Web Notes

## Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN** | A network covering a small area, such as a home, lab or office. | Home Wi-Fi network connecting laptops, smartphones, and a wireless printer. |
| **MAN** | A network covering a city or large campus area. | A city-wide cable television network or a university network spanning multiple campus blocks. |
| **WAN** | A network covering large geographical areas. | The Internet, connecting enterprise networks across countries and continents. |
| **DNS** | Translates a domain name into an IP address. | Translating `google.com` into its corresponding server IP address (e.g., `142.250.190.46`). |
| **Router** | Connects networks and forwards data between them. | A home broadband router linking your local devices to your Internet Service Provider (ISP). |
| **Protocol** | A set of rules devices follow to communicate. | HTTP/HTTPS used by web browsers to transfer and display web pages securely. |
| **Packet switching** | Data is divided into packets that travel across a network. | Streaming a video file by splitting it into small data packets that reassemble on your device. |
| **Client-server** | A client requests a service and a server provides it. | Your web browser (client) requesting a web page from a remote host (server). |

## Task 7.2 — Observe network information

### Terminal Commands Executed:
- **Connectivity Test:** `ping -c 4 youtube.com`
- **DNS Lookup:** `nslookup youtube.com`

### Explanations:
- **What a connectivity test helps you check:**
  A connectivity test verifies whether a remote host or server is reachable across the network, measures round-trip latency (response time), and checks if basic packet routing and transmission are functioning correctly between your machine and the target.
- **What information a DNS lookup displays:**
  A DNS lookup displays the target domain name along with its resolved numeric IP addresses (such as IPv4 `A` records or IPv6 `AAAA` records) and the nameserver used to perform the query.
- **Role of DNS when you enter a website name in a browser:**
  When a user enters a human-readable domain name into a web browser, the DNS acts as the internet's directory service, translating that domain name into the specific numeric IP address required by networking protocols to locate and establish a connection with the target web server.

## Task 7.3 — What happens when you open a website?

### Numbered Explanation (Step-by-Step):
1. **URL Entry & Browser Initiation (Client):** The user enters a web address into the browser address bar, initiating the request from the **client** device[cite: 11].
2. **DNS Lookup (DNS):** The client queries the **DNS** (Domain Name System) to translate the human-readable domain name into the correct numeric IP address of the destination web server[cite: 11].
3. **Network Transmission (Network/Router):** The client's request is packaged into data packets and transmitted through local network switches and **routers**, which forward the packets across the internet infrastructure[cite: 11].
4. **Server Request Receipt (Server):** The target **server** receives the incoming connection request and processes what web page or resource the client is asking for[cite: 11].
5. **Protocol Processing & Response:** Operating under standard web communication **protocols** (such as HTTP/HTTPS), the server compiles the requested website data (HTML, stylesheets, scripts) into response packets[cite: 11].
6. **Delivery & Rendering (Response Displayed):** The response packets travel back across the network to the client, where the web browser receives them, renders the code, and displays the fully formatted website **response to the user**[cite: 11].
