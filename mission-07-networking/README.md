# Mission 7 — How Computers Communicate

## 1. Task / objective
The objective of this mission is to understand core computer networking concepts, conduct safe reachability and DNS lookup experiments using standard macOS Terminal tools, protect personal network privacy, and provide a clear, step-by-step technical explanation of what happens when a user opens a website in a browser.

## 2. Work completed
- Completed the networking concepts table defining LAN, MAN, WAN, DNS, Router, Protocol, Packet Switching, and Client-Server architecture with practical examples.
- Performed a connectivity test using `ping` against the public benchmark domain `example.com`.
- Performed a DNS name resolution lookup using `nslookup` for `example.com`.
- Documented what connectivity and DNS tools confirm and their technical limitations.
- Wrote a structured 6-step walkthrough describing the journey from typing a URL in a browser to the page rendering on screen, correctly incorporating all required networking terms.
- Kept all personal network configurations (local private IP addresses, Wi-Fi SSID, router MAC addresses) completely private and redacted.

## 3. Commands / tools used
- `ping -c 3 example.com`: Sent three ICMP Echo Request packets to check network reachability and round-trip latency.
- `nslookup example.com`: Queried the configured DNS nameserver to resolve the domain name `example.com` into IP addresses (`104.20.23.154` and `172.66.147.243`).

## 4. My understanding

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
|---|---|---|
| **LAN (Local Area Network)** | A network covering a small, geographically localized space, such as a home, school computer lab, or single office building. | A college computer lab where desktop PCs share access to a single networked printer. |
| **MAN (Metropolitan Area Network)** | A network that interconnects users and computing resources across an entire town, city, or large multi-building university campus. | A municipal Wi-Fi network or a city-wide banking network connecting branches across a metropolis. |
| **WAN (Wide Area Network)** | A telecommunications network spanning large geographical distances, connecting multiple cities, countries, or continents. | The global Internet, or a multinational corporate network connecting offices across different continents. |
| **DNS (Domain Name System)** | An internet directory service that translates human-friendly domain names into machine-routable numerical IP addresses. | Translating `example.com` into public IP address `104.20.23.154`. |
| **Router** | A networking device that inspects packet headers and forwards data packets between different computer networks toward their destination. | A home Wi-Fi broadband router connecting home devices (LAN) to the Internet Service Provider (WAN). |
| **Protocol** | A standardized set of rules and conventions determining how data is formatted, transmitted, received, and acknowledged across devices. | HTTP/HTTPS for web page delivery; TCP for reliable byte-stream transport. |
| **Packet switching** | A transmission method where data is segmented into small individual chunks (packets), routed independently across optimal network paths, and reassembled at the receiver. | Sending an image file over the Internet broken down into hundreds of TCP/IP packets. |
| **Client-server** | A distributed computing model where user devices (clients) request services, content, or resources, and centralized host computers (servers) fulfill and respond to those requests. | A student's laptop web browser (client) requesting a web page from a web host server. |

---

### Task 7.2 — Observe network information

#### Connectivity Test (`ping -c 3 example.com`)
```text
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=58 time=10.147 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=58 time=8.548 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=58 time=4.942 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 4.942/7.879/10.147/2.177 ms
```

#### DNS Lookup (`nslookup example.com`)
```text
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	example.com
Address: 172.66.147.243
Name:	example.com
Address: 104.20.23.154
```

#### Analysis
- **What a connectivity test checks**:
  It checks whether the remote host can be reached over the network, whether packets are successfully traveling back and forth, and measures the round-trip latency in milliseconds.
- **What a connectivity test CANNOT establish**:
  It cannot guarantee that the web server software (e.g. Apache or Nginx) or database on the server is running properly or able to serve HTTP requests; it only confirms network-layer reachability. Furthermore, some secure servers block ICMP ping packets even while their web pages are fully functional.
- **What a DNS lookup displays**:
  It displays the DNS server being consulted (`8.8.8.8`) and the corresponding IP address(es) registered for that domain name (`104.20.23.154`).
- **Role of DNS when entering a URL**:
  Humans find domain names like `example.com` easy to memorize, but network routers only route packets using numerical IP addresses. DNS acts like an automated phonebook that resolves the name into an IP address before the browser can even begin establishing a connection.

---

### Task 7.3 — What happens when you open a website?

1. **User Request & Client Action**: The user enters a website URL (e.g., `https://example.com`) into the web browser (**client**).
2. **DNS Resolution**: The client browser checks its local cache, operating system cache, and queries a **DNS** server to translate the hostname into an IP address (`104.20.23.154`).
3. **Connection Handshake**: The client uses the TCP/IP **protocol** to initiate a secure connection (TCP three-way handshake followed by TLS cryptographic handshake) with the server at that IP.
4. **Packet Routing**: Data packets leave the client computer, pass through the local **router**, and travel through multiple intermediary internet routers until reaching the destination.
5. **Server Processing**: The destination web **server** receives the HTTP GET request over the established socket, evaluates the requested resource, and generates an HTTP **response**.
6. **Response Delivery & Browser Rendering**: The server sends the response packets (containing HTML, CSS, and assets) back through the network routers to the client. The browser parses the HTML and renders the web page on the screen for the user.

## 5. Difficulties faced
- Understanding why `nslookup` returned two different IP addresses for `example.com`.

## 6. How I resolved them
- Learned that high-traffic websites configure multiple IP addresses for redundancy and load balancing so that traffic is evenly distributed across servers.

## 7. Evidence / files
- Documented in [mission-07-networking/README.md](file:///Users/musarafakhatun/Desktop/S$AI%20assignment/digital-detective-8013/mission-07-networking/README.md).

## 8. Commit details
- **Commit message**: `Explain networking concepts and website communication`
- **Branch**: `main`
- **Remote status**: Pushed and verified on GitHub.
