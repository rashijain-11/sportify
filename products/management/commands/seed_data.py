from django.core.management.base import BaseCommand
from products.models import Category, Product
from django.contrib.auth.models import User
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seeds database with realistic sports categories, products (INR pricing), and a demo admin user'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Starting Sportify database seeding with Indian Rupee (INR) pricing..."))

        # 1. Create a demo superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@sportify.com', 'admin123')
            self.stdout.write(self.style.SUCCESS("Created demo admin user: username='admin', password='admin123'"))

        # 2. Categories Data
        categories_data = [
            {
                'name': 'Cricket',
                'description': 'Premium cricket bats, leather match balls, protective batting gear, and accessories.',
                'icon': 'bi-trophy',
                'image_url': 'https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Football',
                'description': 'Pro match footballs, goalkeeper gloves, shin guards, boots, and training gear.',
                'icon': 'bi-dribbble',
                'image_url': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Basketball',
                'description': 'Indoor & outdoor composite basketballs, rims, nets, shoes, and jerseys.',
                'icon': 'bi-circle',
                'image_url': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Badminton',
                'description': 'Ultra-light graphite rackets, goose feather shuttlecocks, kit bags, and grips.',
                'icon': 'bi-bullseye',
                'image_url': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Tennis',
                'description': 'High-performance tour tennis rackets, pressurized balls, vibration dampeners, and grips.',
                'icon': 'bi-disc',
                'image_url': 'https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Gym & Fitness',
                'description': 'Dumbbells, resistance bands, speed jump ropes, foam rollers, and strength gear.',
                'icon': 'bi-heart-pulse',
                'image_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Running',
                'description': 'Carbon-plated cushioned running shoes, hydration vests, compression socks, and wear.',
                'icon': 'bi-lightning',
                'image_url': 'https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Sports Accessories',
                'description': 'Insulated stainless steel bottles, gym duffels, wristbands, and stopwatches.',
                'icon': 'bi-backpack',
                'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&auto=format&fit=crop&q=80'
            },
        ]

        created_categories = {}
        for cat_data in categories_data:
            category, _ = Category.objects.update_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            created_categories[category.name] = category

        # 3. Products Data in Indian Rupees (₹)
        products_data = [
            # Cricket
            {
                'category': created_categories['Cricket'],
                'name': 'Apex Pro English Willow Cricket Bat',
                'description': 'Handcrafted Grade 1 English willow cricket bat designed for explosive stroke play. Features an enlarged sweet spot, light pickup, and pre-knocked finish for immediate match readiness.',
                'price': Decimal('7999.00'),
                'discount_price': Decimal('5999.00'),
                'stock': 15,
                'rating': Decimal('4.9'),
                'review_count': 38,
                'is_featured': True,
                'sizes': 'Short Handle, Long Handle, Harrow',
                'image_url': 'https://images.unsplash.com/photo-1531415074868-036b1c57e329?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Cricket'],
                'name': 'Match Grade Leather Cricket Ball (Box of 2)',
                'description': 'Four-piece alum-tanned premium leather ball with pronounced seam for maximum swing and bounce. Ideal for competitive club cricket and multi-day tournaments.',
                'price': Decimal('1499.00'),
                'discount_price': Decimal('1199.00'),
                'stock': 40,
                'rating': Decimal('4.7'),
                'review_count': 22,
                'is_featured': False,
                'sizes': 'Red (Day), White (D/N), Pink',
                'image_url': 'https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Cricket'],
                'name': 'Aero Armor Pro Batting Gloves',
                'description': 'Multi-split finger protection with high-density EVA foam and Pittards sheepskin leather palm for supreme grip and comfort against 90mph bowling.',
                'price': Decimal('1899.00'),
                'discount_price': None,
                'stock': 25,
                'rating': Decimal('4.8'),
                'review_count': 19,
                'is_featured': False,
                'sizes': 'Youth, Men, Extra Large',
                'image_url': 'https://images.unsplash.com/photo-1624880357913-a8539238245b?w=800&auto=format&fit=crop&q=80'
            },

            # Football
            {
                'category': created_categories['Football'],
                'name': 'Strikeforce FIFA Pro Match Football',
                'description': 'Thermally bonded seamless surface construction for more predictable trajectory, enhanced touch, and lower water uptake. Officially approved for tournament play.',
                'price': Decimal('2499.00'),
                'discount_price': Decimal('1899.00'),
                'stock': 30,
                'rating': Decimal('4.9'),
                'review_count': 45,
                'is_featured': True,
                'sizes': 'Size 5 (Standard), Size 4 (Youth)',
                'image_url': 'https://images.unsplash.com/photo-1511886929837-354d827aae26?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Football'],
                'name': 'Vortex Grip Goalkeeper Match Gloves',
                'description': '4mm German contact latex foam offers dependable cushioning and unrivaled stickiness in both wet and dry conditions. Features negative cut finger spines.',
                'price': Decimal('2999.00'),
                'discount_price': Decimal('2399.00'),
                'stock': 20,
                'rating': Decimal('4.8'),
                'review_count': 29,
                'is_featured': False,
                'sizes': 'Size 8, Size 9, Size 10, Size 11',
                'image_url': 'https://images.unsplash.com/photo-1589487391730-58f20eb2c308?w=800&auto=format&fit=crop&q=80'
            },

            # Basketball
            {
                'category': created_categories['Basketball'],
                'name': 'PureBounce All-Court Composite Basketball',
                'description': 'Deep channel grooves and moisture-absorbing micro-fiber composite cover provide superior feel and precision control on indoor hardwood and outdoor concrete courts.',
                'price': Decimal('1999.00'),
                'discount_price': Decimal('1499.00'),
                'stock': 35,
                'rating': Decimal('4.8'),
                'review_count': 34,
                'is_featured': True,
                'sizes': 'Size 7 (Official), Size 6 (Women/Youth)',
                'image_url': 'https://images.unsplash.com/photo-1519861531473-9200262188bf?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Basketball'],
                'name': 'Velocity Slam Breathable Mesh Jersey',
                'description': 'Lightweight moisture-wicking Dri-Tech fabric keeps you cool and dry through fast breaks and overtime. Athletic cut allows unrestricted jumping and shooting motion.',
                'price': Decimal('1299.00'),
                'discount_price': None,
                'stock': 25,
                'rating': Decimal('4.6'),
                'review_count': 16,
                'is_featured': False,
                'sizes': 'S, M, L, XL, XXL',
                'image_url': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800&auto=format&fit=crop&q=80'
            },

            # Badminton
            {
                'category': created_categories['Badminton'],
                'name': 'AeroSpeed Ultra-Light Carbon Racket 4U',
                'description': 'High-modulus Japanese graphite frame with isometric head geometry expands sweet spot by 32%. Engineered for lightning-fast defensive returns and thunderous smashes.',
                'price': Decimal('4999.00'),
                'discount_price': Decimal('3699.00'),
                'stock': 18,
                'rating': Decimal('4.9'),
                'review_count': 41,
                'is_featured': True,
                'sizes': 'G4 (Medium), G5 (Thin)',
                'image_url': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Badminton'],
                'name': 'GrandPrix Goose Feather Shuttlecocks (Tube of 12)',
                'description': 'Selected Grade-A goose feathers mounted on solid natural Portuguese cork base for pinpoint flight stability and true trajectory in competitive matches.',
                'price': Decimal('1499.00'),
                'discount_price': Decimal('1199.00'),
                'stock': 50,
                'rating': Decimal('4.8'),
                'review_count': 53,
                'is_featured': False,
                'sizes': 'Speed 77 (Standard), Speed 78 (Fast)',
                'image_url': 'https://images.unsplash.com/photo-1613918431703-aa6255a6d59b?w=800&auto=format&fit=crop&q=80'
            },

            # Tennis
            {
                'category': created_categories['Tennis'],
                'name': 'TourSpin Master Graphite Tennis Racket',
                'description': 'Engineered with aerodynamic beam design and 100 sq inch head size for extreme top-spin and laser-accurate baseline control. Pre-strung with premium synthetic gut.',
                'price': Decimal('8999.00'),
                'discount_price': Decimal('6999.00'),
                'stock': 12,
                'rating': Decimal('4.9'),
                'review_count': 27,
                'is_featured': True,
                'sizes': 'Grip 2 (4 1/4"), Grip 3 (4 3/8")',
                'image_url': 'https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Tennis'],
                'name': 'Open Championship Tennis Balls (Can of 4)',
                'description': 'Pressurized tournament balls with heavy-duty woven felt cover designed to resist fluffing and maintain consistent bounce on all court surfaces.',
                'price': Decimal('699.00'),
                'discount_price': Decimal('549.00'),
                'stock': 60,
                'rating': Decimal('4.7'),
                'review_count': 36,
                'is_featured': False,
                'sizes': 'Single Can (4 Balls), 3-Pack Bundle',
                'image_url': 'https://images.unsplash.com/photo-1530915534664-4ac6423797c7?w=800&auto=format&fit=crop&q=80'
            },

            # Gym & Fitness
            {
                'category': created_categories['Gym & Fitness'],
                'name': 'HexGrip Rubber Encased Dumbbell Set',
                'description': 'Cast iron core with non-toxic odorless virgin rubber coating to protect floors and reduce noise. Anti-roll hexagonal shape with knurled ergonomic chrome handle.',
                'price': Decimal('3999.00'),
                'discount_price': Decimal('2999.00'),
                'stock': 22,
                'rating': Decimal('4.9'),
                'review_count': 64,
                'is_featured': True,
                'sizes': '5kg Pair, 10kg Pair, 15kg Pair',
                'image_url': 'https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Gym & Fitness'],
                'name': 'ProFlex Resistance Loop Bands (Set of 5)',
                'description': '100% natural Malaysian latex bands offering 5 progressive resistance levels from X-Light (5 lbs) to X-Heavy (40 lbs). Includes mesh travel pouch and workout guide.',
                'price': Decimal('1299.00'),
                'discount_price': Decimal('899.00'),
                'stock': 45,
                'rating': Decimal('4.7'),
                'review_count': 49,
                'is_featured': False,
                'sizes': '5-Band Full Set',
                'image_url': 'https://images.unsplash.com/photo-1598289431512-b97b0917affc?w=800&auto=format&fit=crop&q=80'
            },

            # Running
            {
                'category': created_categories['Running'],
                'name': 'CloudStride Carbon Running Shoes',
                'description': 'Full-length carbon fiber propulsion plate sandwiched in dual-density supercritical foam for ultra-responsive energy return and reduced leg fatigue over marathon distances.',
                'price': Decimal('6999.00'),
                'discount_price': Decimal('4999.00'),
                'stock': 28,
                'rating': Decimal('4.9'),
                'review_count': 58,
                'is_featured': True,
                'sizes': 'UK 7, UK 8, UK 9, UK 10, UK 11',
                'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Running'],
                'name': 'Marathon HydroVent Hydration Vest',
                'description': 'Featherweight 180g breathable mesh vest with dual 500ml front soft flask pockets, rear bladder sleeve, and bounce-free zippered smartphone harness.',
                'price': Decimal('2499.00'),
                'discount_price': Decimal('1899.00'),
                'stock': 20,
                'rating': Decimal('4.8'),
                'review_count': 23,
                'is_featured': False,
                'sizes': 'Small/Medium, Large/X-Large',
                'image_url': 'https://images.unsplash.com/photo-1530549387789-4c1017266635?w=800&auto=format&fit=crop&q=80'
            },

            # Sports Accessories
            {
                'category': created_categories['Sports Accessories'],
                'name': 'HydroArmor Vacuum Insulated Sports Bottle 32oz',
                'description': 'Double-wall 18/8 kitchen-grade stainless steel keeps beverages ice cold for 24 hours or piping hot for 12 hours. Features wide-mouth spout and silicone chug cap.',
                'price': Decimal('1299.00'),
                'discount_price': Decimal('899.00'),
                'stock': 50,
                'rating': Decimal('4.8'),
                'review_count': 72,
                'is_featured': True,
                'sizes': '750ml, 1000ml',
                'image_url': 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Sports Accessories'],
                'name': 'Sportify Waterproof Multi-Pocket Gym Duffel',
                'description': 'Heavy-duty 900D ripstop fabric with dedicated ventilated shoe compartment, wet towel pocket, padded shoulder strap, and key fob clip. 45L capacity.',
                'price': Decimal('2499.00'),
                'discount_price': Decimal('1799.00'),
                'stock': 35,
                'rating': Decimal('4.9'),
                'review_count': 61,
                'is_featured': False,
                'sizes': 'Medium (35L), Large (45L)',
                'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&auto=format&fit=crop&q=80'
            }
        ]

        for p_data in products_data:
            product, created = Product.objects.update_or_create(
                name=p_data['name'],
                defaults=p_data
            )
            action = "Created" if created else "Updated"
            self.stdout.write(f"{action} product: {product.name} (INR {product.price})")

        self.stdout.write(self.style.SUCCESS("Seeding in Indian Rupees (INR) successfully completed!"))
