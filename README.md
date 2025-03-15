# 🎮 Connect 4 AI Agent – Minimax Algorithm

## 📌 Overview
This project implements an **AI agent** for **Connect 4** using the **Minimax Algorithm** with different variations.  
The agent plays against a human player and decides moves based on **game tree search**.  

## 🎯 Features
- **Human vs AI Mode**  
- **Graphical User Interface (GUI)**  
- **AI Algorithm Options:**  
  ✅ **Minimax (No Pruning)**  
  ✅ **Minimax with Alpha-Beta Pruning**  
  ✅ **Expected Minimax** (Probabilistic disc placement)  
- **Game Tree Visualization** (Bonus for GUI representation)  

## 🧠 AI Implementation Details
- **Minimax Algorithm**: AI searches for the best move using a recursive game tree.  
- **Alpha-Beta Pruning**: Optimizes Minimax by eliminating unnecessary branches.  
- **Expected Minimax**: Considers **probabilistic disc placement (60% in chosen column, 40% in adjacent columns)**.  
- **Heuristic Evaluation**:  
  - Assigns a score based on game state.  
  - Determines which player is closer to winning.  
  - Uses **truncation depth (K)** to limit search depth.  

## 📊 Performance Evaluation
- **Comparison of AI strategies** based on:  
  ✅ Time taken per move  
  ✅ Nodes expanded at different **K-values**  
- **Sample minimax tree outputs** printed in a traceable format.  

