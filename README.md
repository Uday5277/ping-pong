**🏓 Ping Pong Game (Python + Pygame)**

A fast-paced real-time Ping Pong game built using Python and Pygame, featuring responsive paddle controls, sound feedback, and a replay system with multiple match modes.

**🎮 Features**

✅ Smooth gameplay with player vs AI
✅ Ball-paddle and wall collision detection (improved for high speed)
✅ Score tracking and Game Over screen
✅ Replay Menu — choose between:

Best of 3
Best of 5
Best of 7
✅ Sound Effects

Paddle hit

Wall bounce

**Score sound**
✅ Simple AI opponent that tracks the ball
✅ Keyboard controls:

W → Move paddle up

S → Move paddle down

ESC → Exit game or replay menu

**🧩 Project Structure**
pygame-pingpong/
├── main.py
├── requirements.txt
├── game/
│   ├── game_engine.py
│   ├── paddle.py
│   └── ball.py
├── assets/
│   └── sounds/
│       ├── paddle_hit.wav
│       ├── wall_bounce.wav
│       └── score.wav
└── README.md

**⚙️ Installation & Setup**
1. Clone this repository
git clone https://github.com/YOUR_USERNAME/ping-pong.git
cd ping-pong

2. Create & activate a virtual environment (recommended)
python -m venv .venv
# Activate (Windows)
.venv\Scripts\activate
# Activate (Mac/Linux)
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

**▶️ How to Play**

Run the main game file:

python main.py


Use the keyboard:

W / S — move your paddle up and down

ESC — exit the game or cancel replay

When either player reaches the target score (default 5), a Game Over screen appears.
You can then choose to replay by selecting a mode:

Press 3 → Best of 3

Press 5 → Best of 5

Press 7 → Best of 7

Press ESC → Exit the game
