# CINN
Combinatorial Informed Neural Network aka pinnnns on a l-o-t-t-e-r-y urnnn model w/o replacement

so some typos to avoid key word search hits .. i think 1/4 of all network hits are now ai engines/agents probing the internet  .. this feels like a bad 1970's tv now.... i need a used car now too...

In claude:
  a pinn transformer model: physics informed neural network using the fluid flow equations (volterra/Stokes/) is now a standard in aerodynamic simulations. Is there a combinatoric informed neural network to train on data from a urn model w/o replacement? hypergeometric distribution is known; the urn model draws are random against that dist ... your training on that data to determine a range of next state draws on that urn model. write a pytorch transformer model for that prediction
  
In google aistudio console which is gemini3-pro-preview(cli is still 2.5): same thing prompt but this time ask for tensorflow python code

in copilot a lot of gibberish .. but i'm only on the browser maybe the paid-for-chatgpt access is different .. i almost never use copilot except in vs2022/25

pytorch is on cuda13.0 but tf is back to ancient py and cuda 11....  try a wslub24 conda shell for that one.

toolcalling for current paper references is neat but some of the refs look strange.  google must be all stanford guys it will ref last Monday's urn prob talk but not the actual content just the poster announcement...so why is that a reference in this tool search? claude is shorter but again the tool agent is searching papers in 2025 even if they are iffy...

as always mrphelps if your caught or ki.... published ai generated slop will lead to model collapse and the end of the universe and we will disclaim any knowledge and blame the trumper's...

working on a data loader now for the two provided scripts
i will say in the past 20 years i've spent months writing web spiders to gather data ... in claude the spiders were rewritten in an hour..sure i remembered to set a primarykey to prevent duplicate rows in duckdb .. but otherwise 1 hour done ... not months of tuning html tag regex's; and rewriting them every few years...

oh i got about 10million rows... of 80/20 urn model draws..

20251227
https://www.merriam-webster.com/dictionary/slop
so after 2 weeks of hand tuning and refining to a working script in prod is "refined and tested slop ai" better than "ai slop"? 700 lines of python works; i manually changed the time.sleep(33) instead of .2 so it takes 12 hours to run.  As web spider practice i did two tracks one playwright and one selenium using both gemini3-pro preview cli and claude web.  In all cases playwright took 3 times longer to get to a working webspider....and constantly proclaimed that playwright was a modern tool to handle dynamic pages.  The selenium versions after a few fixups that i never knew were possible wacked out a working script in 1/3 1/4 of the time.  Is this because of the volume of microsoft playwright gibberish in the training data by the winwinnies on a tool that almost wasn't?  I was surprised that the wpf project tripped up on win shell commands when all examples of wpf are on windows .. the training examples from linux infected basic 
win console cmds in gemini 2.5 and even 3.  Copilot has a huge safety tool filter and would refuse to do the most basic sites ... apparently they
detected a terms of use on the site and said nope...
Anyway a few more sites to spider into duckdb and mariadb ... then a dataloader into the transformer models .. even 20 million rows encoded is doable on 
a 32g vram gpu.

20260406
well i guess teo is right the lower 2 quantiles are cooked...
huggingface-cli download Qwen/Qwen2.5-Coder-32B-Instruct --local-dir /workspace/models/qwen35-coder-32b-instruct
and webui gets me a plusing icon for hours after a code prompt... 124g of memory used on the asus gx10 box...and i got ports messed up all over the place ... 3 clients reboot constantly to clear the ports.  I guess i got to try the quantized models now
cinn training by the way takes 3 weeks on a rtx5090 box to move from 4.6 to 3.2 loss ... it pretty much is stuck; trying 16 layers instead of 4 now but it looks to be combinatorics is combinatorics .. it ain't going to converge.

20260425
well 24 layers and 32 layers throw a cuda memory error on a rtx5090 w/ 8 other small cuda pty loaded simulation jobs running .. blocksize 8192
and takes up a full 32g memory and the shared gpu memory to 64g is actually used by the other jobs ... but throws cuda memory errors.  After 75 epochs crashed and i went back to 16 layers ... but both jobs do not converge loss pass 3.2; in
fact they bounce off that and go to 3.4loss so real 554k rows of data; and 1.9 million rows both stuck at 3.2 loss.
copilot is giving me the huggingface downloads for the asus gx10-gb10 and pulled down qwen36-35b-a3b and gemma4-27b- ... and i have to use copilot to make a template prompt to get python code for a simple combinatorics math prompt ... none of the freebie browser ai engines are that picky ...  i mean it is maybe 30 minutes with claude freebie ... or a few hours with local qwen; yeah i use up my freebie tokens but local ai is very picky...i thought the model was broken...and oddly copilot leads me out of the wilderness...
