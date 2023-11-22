from typing import Type 
import ttkbootstrap as ttk

class CustomStyles:

    
    def __init__(
        self: Type['CustomStyles']
    ) -> None:
        
        self.style = ttk.Style()

        # --Success TButton!--
        self.style.configure(
            style='big.success.TButton', 
            font=('Helvetica', 16, 'bold'),
            width=10,
            padding=(0, 10)
        )
        self.style.configure(
            style='medium.success.TButton', 
            font=('Helvetica', 14, 'bold'),
            width=8,
            padding=(0, 8)
        )
        self.style.configure(
            style='small.success.TButton', 
            font=('Helvetica', 12, 'bold'),
            width=6,
            padding=(0, 6)
        )

        # --Danger TButton!--
        self.style.configure(
            style='big.danger.TButton', 
            font=('Helvetica', 16, 'bold'),
            width=10,
            padding=(0, 10)
        )
        self.style.configure(
            style='medium.danger.TButton', 
            font=('Helvetica', 14, 'bold'),
            width=8,
            padding=(0, 8)
        )
        self.style.configure(
            style='small.danger.TButton', 
            font=('Helvetica', 12, 'bold'),
            width=6,
            padding=(0, 6)
        )

        # --Info TButton!--
        self.style.configure(
            style='big.info.TButton', 
            font=('Helvetica', 16, 'bold'),
            width=10,
            padding=(0, 10)
        )
        self.style.configure(
            style='medium.info.TButton', 
            font=('Helvetica', 14, 'bold'),
            width=8,
            padding=(0, 8)
        )
        self.style.configure(
            style='small.info.TButton', 
            font=('Helvetica', 12, 'bold'),
            width=6,
            padding=(0, 6)
        )
        